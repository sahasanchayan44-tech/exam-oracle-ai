import pytest
from app.services.statistical_intelligence.descriptive import DescriptiveStatisticsEngine
from app.services.statistical_intelligence.correlation import CorrelationEngine
from app.services.statistical_intelligence.information_theory import InformationTheoryEngine
from app.services.statistical_intelligence.bayesian_uncertainty import BayesianUncertaintyEngine
from app.services.statistical_intelligence.trend_time_series import TimeSeriesTrendEngine
from app.services.statistical_intelligence.pattern_mining import PatternMiningEngine
from app.services.statistical_intelligence.auto_benchmark import AutoBenchmarkingEngine
from app.services.statistical_intelligence.ensemble import EnsembleSystemEngine
from app.services.statistical_intelligence.intelligence_facade import StatisticalIntelligenceFacade

def test_descriptive_stats():
    data = [10.0, 15.0, 20.0, 25.0, 30.0]
    res = DescriptiveStatisticsEngine.calculate_stats(data)
    assert res.mean == 20.0
    assert res.std_dev > 0.0
    assert res.sample_size == 5

def test_correlation_analysis():
    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    y = [2.0, 4.0, 6.0, 8.0, 10.0]
    res = CorrelationEngine.analyze_correlation(x, y)
    assert res.pearson_coefficient == 1.0
    assert res.spearman_coefficient == 1.0

def test_information_theory():
    p = [0.5, 0.5]
    q = [0.5, 0.5]
    res = InformationTheoryEngine.analyze_information_metrics(p, q)
    assert res.entropy_bits == 1.0
    assert res.kl_divergence == 0.0

def test_bayesian_uncertainty():
    obs = [0.6, 0.7, 0.65, 0.8]
    res = BayesianUncertaintyEngine.analyze_uncertainty(obs)
    assert 0.0 <= res.posterior_probability <= 1.0
    assert res.bootstrap_ci_lower <= res.bootstrap_ci_upper
    assert res.prediction_interval_lower <= res.prediction_interval_upper

def test_trend_analysis():
    series = [10.0, 12.0, 15.0, 18.0, 22.0]
    res = TimeSeriesTrendEngine.analyze_series(series)
    assert len(res.sma) == 5
    assert len(res.ema) == 5
    assert res.detected_trend_direction in ["INCREASING", "DECREASING", "STABLE"]

def test_pattern_mining():
    txs = [
        ["Trees", "Recursion"],
        ["Trees", "Recursion", "Binary Search"],
        ["Graphs", "BFS"],
    ]
    res = PatternMiningEngine.mine_patterns(txs)
    assert len(res.frequent_itemsets) > 0

@pytest.mark.asyncio
async def test_intelligence_facade():
    facade = StatisticalIntelligenceFacade()
    res = await facade.execute_full_statistical_analysis([])
    assert res.best_benchmarked_model is not None
    assert len(res.feature_importances) > 0
    assert len(res.historical_evidence_rationale) > 0
