import pytest
import numpy as np
from app.services.automl.hpo import HyperparameterOptimizer
from app.services.automl.framework import AutoMLFramework
from app.services.advanced_stats.bayesian_inference import AdvancedBayesianInferenceEngine
from app.services.advanced_stats.hypothesis_testing import HypothesisTestingSuite
from app.services.advanced_stats.multivariate import MultivariateStatisticsEngine
from app.services.advanced_time_series.classical import ClassicalTimeSeriesEngine
from app.services.nlp_platform.embeddings import AdvancedEmbeddingRegistry
from app.services.calibration_explainability.calibration import ModelCalibrationEngine
from app.services.research_orchestrator.research_engine import MasterResearchAutoMLEngine

def test_hpo_optuna():
    X = np.random.randn(20, 4)
    y = np.random.choice([0, 1], size=20)
    res = HyperparameterOptimizer.optimize_optuna(X, y, n_trials=3)
    assert res.best_score > 0
    assert res.optimization_method is not None

def test_automl_framework():
    X = np.random.randn(20, 4)
    y = np.random.choice([0, 1], size=20)
    records = AutoMLFramework.run_automl_benchmark(X, y)
    assert len(records) > 0
    assert records[0].cpu_usage_pct >= 0.0

def test_mcmc_metropolis_hastings():
    obs = [5.0, 7.0, 6.0, 8.0]
    res = AdvancedBayesianInferenceEngine.run_mcmc_metropolis_hastings(obs, num_samples=100, burn_in=20)
    assert res.posterior_mean > 0
    assert res.credible_interval_lower <= res.credible_interval_upper

def test_hypothesis_testing_suite():
    s1 = [10.0, 12.0, 14.0, 15.0]
    s2 = [8.0, 11.0, 13.0, 12.0]
    results = HypothesisTestingSuite.run_all_tests(s1, s2)
    assert len(results) >= 5

def test_multivariate_decomposition():
    X = np.random.randn(20, 4)
    res = MultivariateStatisticsEngine.decompose_multivariate(X)
    assert len(res.pca_explained_variance_ratio) > 0

@pytest.mark.asyncio
async def test_master_research_automl_pipeline():
    engine = MasterResearchAutoMLEngine()
    res = await engine.execute_research_pipeline()
    assert len(res.automl_experiment_records) > 0
    assert res.selected_embedding_model is not None
    assert res.recommended_model_or_ensemble is not None
