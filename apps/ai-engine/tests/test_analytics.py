import pytest
from app.services.statistical.kde_forecaster import KDEProbabilisticForecaster

@pytest.mark.asyncio
async def test_kde_probabilistic_forecaster():
    forecaster = KDEProbabilisticForecaster()
    obs = [
        {"topic_id": "t1", "topic_name": "Trees", "marks": 10},
        {"topic_id": "t1", "topic_name": "Trees", "marks": 15},
        {"topic_id": "t2", "topic_name": "Graphs", "marks": 5},
    ]
    result = await forecaster.compute_forecast(obs)
    assert result.sample_size == 3
    assert len(result.forecasts) == 2
    for f in result.forecasts:
        assert 0.0 <= f.estimated_probability <= 1.0
        assert f.confidence_lower_bound <= f.confidence_upper_bound
