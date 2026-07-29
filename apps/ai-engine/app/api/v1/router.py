from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.config import settings

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    disclaimer: str

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="HEALTHY",
        service=settings.PROJECT_NAME,
        version="1.0.0",
        disclaimer=settings.NON_PREDICTIVE_DISCLAIMER,
    )
