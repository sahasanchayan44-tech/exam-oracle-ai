from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from app.services.statistical_intelligence.intelligence_facade import (
    StatisticalIntelligenceFacade,
    StatisticalIntelligenceResponse,
)

router = APIRouter(prefix="/stats-intelligence", tags=["Statistical Intelligence Engine"])
facade = StatisticalIntelligenceFacade()

class AnalysisRequest(BaseModel):
    target_concept: Optional[str] = "Data Structures & Algorithms"
    historical_data: List[Dict[str, Any]] = []

@router.post("/analyze", response_model=StatisticalIntelligenceResponse)
async def analyze_statistical_intelligence(payload: AnalysisRequest):
    """
    Executes full Statistical Intelligence Suite:
    - Descriptive Statistics (Mean, Median, Mode, Variance, Covariance)
    - Correlation Analysis (Pearson, Spearman, Kendall, Partial Correlation)
    - Information Theory (Entropy, Cross-Entropy, KL/JS Divergence, Mutual Info, Chi-Square, Cramér's V)
    - Bayesian Statistics & Uncertainty (Posterior, Monte Carlo, Bootstrap, 95% CI, Prediction Intervals)
    - Time Series Trends (SMA, EMA, ARIMA, STL, CUSUM, Change Points)
    - Pattern Mining (Apriori, FP-Growth, Association Rules)
    - ML Auto-Benchmarking (Grid/Random/Bayesian CV selection across 10 models)
    - Multi-Strategy Ensemble (Voting, Stacking, Weighted Ensemble)
    """
    try:
        return await facade.execute_full_statistical_analysis(
            historical_paper_data=payload.historical_data,
            target_concept=payload.target_concept,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Statistical Intelligence Analysis failed: {str(e)}")
