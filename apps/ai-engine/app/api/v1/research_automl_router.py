from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.research_orchestrator.research_engine import (
    MasterResearchAutoMLEngine,
    MasterResearchEngineResult,
)

router = APIRouter(prefix="/research-automl", tags=["Master Research AutoML Engine"])
research_engine = MasterResearchAutoMLEngine()

class ResearchPipelineRequest(BaseModel):
    dataset_name: Optional[str] = "GATE_CS_Historical_Exam_Papers"
    target_task: Optional[str] = "topic_probability_estimation"

@router.post("/execute", response_model=MasterResearchEngineResult)
async def execute_research_automl_pipeline(payload: ResearchPipelineRequest):
    """
    Executes the research-grade AutoML & Statistical Intelligence Platform:
    - AutoML Benchmarking (FLAML, AutoGluon, H2O, TPOT, Auto-Sklearn)
    - Optuna & Hyperband Hyperparameter Optimization
    - MLflow Experiment & Resource Logging (CPU, Memory, Training/Inference Time)
    - Dynamic Embedding Model Selection (BERT, RoBERTa, DeBERTa, SBERT, Instructor, E5)
    - MCMC Bayesian Sampling & Gaussian Process Regression
    - Hypothesis Testing Suite (Student t-test, Welch, ANOVA, Mann-Whitney, KS, Shapiro-Wilk)
    - Multivariate Decompositions (PCA, FastICA, Factor Analysis, LDA)
    - Time Series Forecasting (ARIMA, SARIMA, Holt-Winters, Neural LSTM/GRU, Change Point)
    - Knowledge Graph AI Algorithms (PageRank, Louvain, GNN Embeddings)
    - Probability Calibration (Platt Scaling, Isotonic Regression, Temperature Scaling, Brier Score)
    - SHAP & LIME Feature Explainability
    """
    try:
        return await research_engine.execute_research_pipeline(
            dataset_name=payload.dataset_name, target_task=payload.target_task
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Research AutoML Execution failed: {str(e)}")
