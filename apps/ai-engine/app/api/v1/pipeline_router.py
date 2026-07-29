from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from app.services.ocr.ocr_service import OCRService
from app.services.extractor.question_extractor import QuestionExtractorService
from app.services.llm.classifier import QuestionClassifierService
from app.services.embeddings.vector_service import VectorEmbeddingService
from app.services.knowledge_graph.graph_service import KnowledgeGraphService
from app.services.statistical.feature_engineering import FeatureEngineeringService
from app.services.statistical.kde_forecaster import KDEProbabilisticForecaster
from app.services.generation.question_synthesizer import QuestionSynthesizerService
from app.core.config import settings

router = APIRouter(prefix="/pipeline", tags=["End-to-End AI Pipeline"])

ocr_service = OCRService()
extractor_service = QuestionExtractorService()
classifier_service = QuestionClassifierService()
vector_service = VectorEmbeddingService()
graph_service = KnowledgeGraphService()
feature_service = FeatureEngineeringService()
kde_service = KDEProbabilisticForecaster()
synthesizer_service = QuestionSynthesizerService()

class PipelineExecutionResponse(BaseModel):
    status: str
    ocr_engine_used: str
    extracted_questions_count: int
    classified_questions: List[Dict[str, Any]]
    graph_metrics: Dict[str, Any]
    forecast_results: Dict[str, Any]
    synthesized_practice_questions: List[Dict[str, Any]]
    disclaimer: str

@router.post("/execute", response_model=PipelineExecutionResponse)
async def execute_full_pipeline(
    file: Optional[UploadFile] = File(None),
    raw_text: Optional[str] = Form(None),
    ocr_engine: Optional[str] = Form("tesseract"),
    llm_provider: Optional[str] = Form("openai"),
):
    """
    Executes the entire async AI pipeline:
    PDF/Image OCR -> Question Extraction -> LLM Multi-level Classification -> Qdrant Embedding Indexing ->
    Knowledge Graph PageRank & Node2Vec -> Feature Engineering -> Bayesian KDE Forecast -> Practice Question Synthesis.
    """
    try:
        # Step 1: OCR / Input Text Acquisition
        if file:
            content = await file.read()
            ocr_res = await ocr_service.process_document(content, preferred_engine=ocr_engine)
            text = ocr_res.full_text
            engine_used = ocr_res.engine_name
        elif raw_text:
            text = raw_text
            engine_used = "direct_text_input"
        else:
            text = "Q1. Derive the time complexity of QuickSort in worst and best cases. [10 marks]\nQ2. Explain Binary Search Trees traversal. [5 marks]"
            engine_used = "sample_fallback"

        # Step 2: Question Extraction
        questions = await extractor_service.extract_questions(text)

        # Step 3: LLM Classification & Step 4: Embedding Indexing
        classified_list = []
        q_dicts_for_graph = []

        for q in questions:
            cls_res = await classifier_service.classify_question(q.content, provider_name=llm_provider)
            
            # Store in Qdrant Vector DB
            vec_id = await vector_service.store_question_vector(
                question_id=f"q_{q.question_number}",
                text=q.content,
                payload={"concept": cls_res.concept, "difficulty": cls_res.difficulty},
            )

            q_dict = {
                "id": f"q_{q.question_number}",
                "content": q.content,
                "marks": q.marks,
                "equations": q.equations,
                "options": q.options,
                "is_numerical": q.is_numerical,
                "classification": cls_res.dict(),
                "vector_id": vec_id,
            }
            classified_list.append(q_dict)
            q_dicts_for_graph.append(
                {"id": f"q_{q.question_number}", "concept": cls_res.concept, "chapter": cls_res.chapter, "tagged_concepts": cls_res.tagged_concepts}
            )

        # Step 5: Knowledge Graph (PageRank, Community Detection & Node2Vec)
        graph_res = await graph_service.build_knowledge_graph(q_dicts_for_graph)

        # Step 6 & 7: Feature Engineering & Bayesian KDE Forecast
        obs = [
            {"topic_id": q["classification"]["concept"], "topic_name": q["classification"]["concept"], "marks": q["marks"]}
            for q in classified_list
        ]
        forecast_res = await kde_service.compute_forecast(obs)

        # Step 8: Question Synthesis
        synthesized_list = []
        if classified_list:
            top_q = classified_list[0]
            synth = await synthesizer_service.synthesize_practice_question(
                topic_name=top_q["classification"]["concept"],
                seed_question_text=top_q["content"],
                target_marks=top_q["marks"],
                provider_name=llm_provider,
            )
            synthesized_list.append(synth.dict())

        return PipelineExecutionResponse(
            status="SUCCESS",
            ocr_engine_used=engine_used,
            extracted_questions_count=len(questions),
            classified_questions=classified_list,
            graph_metrics={
                "num_nodes": graph_res.num_nodes,
                "num_edges": graph_res.num_edges,
                "communities_count": len(graph_res.communities),
                "top_pagerank": list(graph_res.pagerank_scores.items())[:3],
            },
            forecast_results=forecast_res.dict(),
            synthesized_practice_questions=synthesized_list,
            disclaimer=settings.NON_PREDICTIVE_DISCLAIMER,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pipeline execution failed: {str(e)}")
