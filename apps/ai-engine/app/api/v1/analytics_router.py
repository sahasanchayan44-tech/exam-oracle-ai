from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from app.services.statistical.kde_forecaster import KDEProbabilisticForecaster, ProbabilisticForecastResult
from app.services.statistical.feature_engineering import FeatureEngineeringService, EngineeredFeatures

router = APIRouter(prefix="/analytics", tags=["Statistical Analytics & KDE Forecasting"])
kde_service = KDEProbabilisticForecaster()
feature_service = FeatureEngineeringService()

class ForecastRequest(BaseModel):
    observations: List[Dict[str, Any]]
    confidence_level: float = 0.95

class FeatureRequest(BaseModel):
    question_text: str
    bloom_level: str
    year: int

@router.post("/forecast", response_model=ProbabilisticForecastResult)
async def forecast_topic_probabilities(payload: ForecastRequest):
    """
    Computes Bayesian Kernel Density Estimation (KDE) topic coverage probability distributions
    with 95% confidence intervals and explainable statistical evidence.
    """
    try:
        return await kde_service.compute_forecast(
            historical_observations=payload.observations,
            confidence_level=payload.confidence_level,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"KDE Probabilistic Forecast failed: {str(e)}")

@router.post("/features", response_model=EngineeredFeatures)
async def extract_features(payload: FeatureRequest):
    """
    Computes syntactic complexity, difficulty index, bloom weight, and temporal decay features.
    """
    try:
        return await feature_service.compute_features(
            question_text=payload.question_text,
            bloom_level=payload.bloom_level,
            year=payload.year,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Feature calculation failed: {str(e)}")
