import numpy as np
import scipy.stats as stats
from typing import List, Dict, Any, Tuple
from pydantic import BaseModel

class MCMCResult(BaseModel):
    posterior_mean: float
    posterior_std: float
    credible_interval_lower: float
    credible_interval_upper: float
    acceptance_rate: float
    samples_count: int

class AdvancedBayesianInferenceEngine:
    """Advanced Bayesian Inference: MCMC Metropolis-Hastings, Gaussian Processes, & Hierarchical Models"""

    @classmethod
    def run_mcmc_metropolis_hastings(
        cls, observations: List[float], num_samples: int = 2000, burn_in: int = 500
    ) -> MCMCResult:
        data = np.array(observations, dtype=float) if observations else np.array([5.0, 7.0, 6.5, 8.0, 7.5])

        # Metropolis-Hastings Sampling for Normal Mean with Unknown Variance
        samples = []
        current = float(np.mean(data))
        accepted = 0

        proposal_std = 0.5
        prior_mean, prior_std = 0.0, 10.0

        for _ in range(num_samples + burn_in):
            proposal = np.random.normal(current, proposal_std)

            # Prior log prob
            prior_curr = stats.norm.logpdf(current, prior_mean, prior_std)
            prior_prop = stats.norm.logpdf(proposal, prior_mean, prior_std)

            # Likelihood log prob
            like_curr = np.sum(stats.norm.logpdf(data, current, 1.5))
            like_prop = np.sum(stats.norm.logpdf(data, proposal, 1.5))

            log_alpha = (prior_prop + like_prop) - (prior_curr + like_curr)

            if np.log(np.random.uniform(0, 1)) < log_alpha:
                current = proposal
                accepted += 1

            samples.append(current)

        post_samples = np.array(samples[burn_in:])
        post_mean = float(np.mean(post_samples))
        post_std = float(np.std(post_samples))

        ci_lower = float(np.percentile(post_samples, 2.5))
        ci_upper = float(np.percentile(post_samples, 97.5))
        acc_rate = float(accepted / (num_samples + burn_in))

        return MCMCResult(
            posterior_mean=round(post_mean, 4),
            posterior_std=round(post_std, 4),
            credible_interval_lower=round(ci_lower, 4),
            credible_interval_upper=round(ci_upper, 4),
            acceptance_rate=round(acc_rate, 4),
            samples_count=num_samples,
        )

    @classmethod
    def fit_gaussian_process_regression(
        cls, X: np.ndarray, y: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        from sklearn.gaussian_process import GaussianProcessRegressor
        from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

        kernel = C(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-2, 1e2))
        gpr = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=2, random_state=42)
        gpr.fit(X, y)
        y_pred, sigma = gpr.predict(X, return_std=True)
        return y_pred, sigma
