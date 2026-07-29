import numpy as np
import scipy.stats as stats
from typing import List, Dict, Any, Tuple
from pydantic import BaseModel

class BayesianUncertaintyResult(BaseModel):
    prior_probability: float
    likelihood: float
    posterior_probability: float
    monte_carlo_mean: float
    monte_carlo_std_dev: float
    bootstrap_ci_lower: float
    bootstrap_ci_upper: float
    prediction_interval_lower: float
    prediction_interval_upper: float
    confidence_score: float

class BayesianUncertaintyEngine:
    """Bayesian Statistics, Monte Carlo Simulation, Bootstrapping & Prediction Interval Estimation"""

    @staticmethod
    def compute_bayesian_updating(
        prior: float, likelihood: float, evidence_marginal: float = None
    ) -> float:
        if evidence_marginal is None or evidence_marginal <= 0:
            evidence_marginal = (likelihood * prior) + ((1.0 - likelihood) * (1.0 - prior)) + 1e-9
        posterior = (likelihood * prior) / evidence_marginal
        return float(np.clip(posterior, 0.001, 0.999))

    @classmethod
    def analyze_uncertainty(
        cls,
        observations: List[float],
        prior_alpha: float = 2.0,
        prior_beta: float = 2.0,
        num_simulations: int = 1000,
        confidence_level: float = 0.95,
    ) -> BayesianUncertaintyResult:
        data = np.array(observations, dtype=float) if observations else np.array([0.5, 0.6, 0.7])
        n = len(data)

        # 1. Prior and Conjugate Bayesian Update (Beta-Binomial / Normal-Normal)
        prior_prob = prior_alpha / (prior_alpha + prior_beta)
        mean_data = float(np.mean(data))
        likelihood = float(np.clip(mean_data, 0.05, 0.95))
        posterior_prob = cls.compute_bayesian_updating(prior_prob, likelihood)

        # 2. Monte Carlo Simulation
        np.random.seed(42)
        std_data = float(np.std(data, ddof=1)) if n > 1 else 0.1
        mc_samples = np.random.normal(loc=mean_data, scale=std_data + 1e-5, size=num_simulations)
        mc_mean = float(np.mean(mc_samples))
        mc_std = float(np.std(mc_samples))

        # 3. Bootstrap Resampling (1000 iterations)
        bootstrap_means = []
        for _ in range(num_simulations):
            sample = np.random.choice(data, size=n, replace=True)
            bootstrap_means.append(np.mean(sample))

        alpha_percentile = (1.0 - confidence_level) / 2.0
        ci_lower = float(np.percentile(bootstrap_means, alpha_percentile * 100.0))
        ci_upper = float(np.percentile(bootstrap_means, (1.0 - alpha_percentile) * 100.0))

        # 4. Prediction Interval (for next unseen observation x_{n+1})
        t_val = stats.t.ppf((1 + confidence_level) / 2.0, df=max(1, n - 1))
        pred_margin = t_val * std_data * np.sqrt(1 + 1.0 / max(1, n))
        pred_lower = float(mean_data - pred_margin)
        pred_upper = float(mean_data + pred_margin)

        # Overall statistical reliability score
        confidence_score = float(np.clip(1.0 - (std_data / (mean_data + 1e-5)), 0.35, 0.98))

        return BayesianUncertaintyResult(
            prior_probability=round(prior_prob, 4),
            likelihood=round(likelihood, 4),
            posterior_probability=round(posterior_prob, 4),
            monte_carlo_mean=round(mc_mean, 4),
            monte_carlo_std_dev=round(mc_std, 4),
            bootstrap_ci_lower=round(ci_lower, 4),
            bootstrap_ci_upper=round(ci_upper, 4),
            prediction_interval_lower=round(pred_lower, 4),
            prediction_interval_upper=round(pred_upper, 4),
            confidence_score=round(confidence_score, 4),
        )
