from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.llm.classifier import QuestionClassifierService
from app.services.llm.schemas import QuestionClassificationResult

router = APIRouter(prefix="/classification", tags=["LLM Question Classification"])
classifier_service = QuestionClassifierService()

class ClassifyRequest(BaseModel):
    question_text: str
    provider: Optional[str] = "openai" # Supported: openai, claude, gemini, llama, mistral, qwen, deepseek

@router.post("/classify", response_model=QuestionClassificationResult)
async def classify_question(payload: ClassifyRequest):
    """
    Classifies a question using the specified LLM provider across multi-level taxonomy:
    Subject, Chapter, Subchapter, Concept, Formulae, Difficulty, Bloom's Taxonomy, Question Type, & Solving Time.
    """
    try:
        return await classifier_service.classify_question(
            question_text=payload.question_text, provider_name=payload.provider
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Classification failed: {str(e)}")
