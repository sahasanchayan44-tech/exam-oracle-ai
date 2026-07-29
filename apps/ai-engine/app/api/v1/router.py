from fastapi import APIRouter
from pydantic import BaseModel
from app.core.config import settings

from app.api.v1.ocr_router import router as ocr_router
from app.api.v1.extraction_router import router as extraction_router
from app.api.v1.classification_router import router as classification_router
from app.api.v1.graph_router import router as graph_router
from app.api.v1.analytics_router import router as analytics_router
from app.api.v1.synthesis_router import router as synthesis_router
from app.api.v1.pipeline_router import router as pipeline_router
from app.api.v1.statistical_intelligence_router import router as statistical_intelligence_router
from app.api.v1.research_automl_router import router as research_automl_router

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    disclaimer: str

@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    return HealthResponse(
        status="HEALTHY",
        service=settings.PROJECT_NAME,
        version="1.0.0",
        disclaimer=settings.NON_PREDICTIVE_DISCLAIMER,
    )

# Include All Microservice Routers
router.include_router(ocr_router)
router.include_router(extraction_router)
router.include_router(classification_router)
router.include_router(graph_router)
router.include_router(analytics_router)
router.include_router(synthesis_router)
router.include_router(pipeline_router)
router.include_router(statistical_intelligence_router)
router.include_router(research_automl_router)
