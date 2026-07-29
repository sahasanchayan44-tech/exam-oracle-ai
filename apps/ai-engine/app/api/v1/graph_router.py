from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from app.services.knowledge_graph.graph_service import KnowledgeGraphService, GraphAnalysisResult

router = APIRouter(prefix="/graph", tags=["Knowledge Graph Engine"])
graph_service = KnowledgeGraphService()

class GraphBuildRequest(BaseModel):
    questions: List[Dict[str, Any]]

@router.post("/build", response_model=GraphAnalysisResult)
async def build_graph(payload: GraphBuildRequest):
    """
    Builds a concept co-occurrence knowledge graph.
    Executes PageRank centrality, Community Detection, and Node2Vec embedding generation.
    Returns D3-ready graph payload.
    """
    try:
        return await graph_service.build_knowledge_graph(payload.questions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Knowledge Graph creation failed: {str(e)}")
