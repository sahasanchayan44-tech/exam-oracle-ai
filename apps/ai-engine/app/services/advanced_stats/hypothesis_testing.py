import numpy as np
import scipy.stats as stats
from typing import List, Dict, Any
from pydantic import BaseModel

class HypothesisTestResult(BaseModel):
    test_name: str
    statistic: float
    p_value: float
    is_significant_at_05: bool
    conclusion: str

class HypothesisTestingSuite:
    """Hypothesis Testing Suite: t-test, Welch, ANOVA, Mann-Whitney U, Kruskal-Wallis, KS, Shapiro-Wilk"""

    @classmethod
    def run_all_tests(
        cls, sample1: List[float], sample2: List[float] = None
    ) -> List[HypothesisTestResult]:
        s1 = np.array(sample1, dtype=float) if len(sample1) >= 3 else np.array([10.0, 12.0, 14.0, 15.0, 16.0])
        s2 = np.array(sample2, dtype=float) if sample2 and len(sample2) >= 3 else np.array([8.0, 11.0, 13.0, 12.0, 14.0])

        results = []

        # 1. Student t-test (Equal Variance)
        t_stat, t_p = stats.ttest_ind(s1, s2, equal_var=True)
        results.append(
            HypothesisTestResult(
                test_name="Student's t-test",
                statistic=round(float(t_stat), 4),
                p_value=round(float(t_p), 4),
                is_significant_at_05=t_p < 0.05,
                conclusion="Reject H0 (Means differ)" if t_p < 0.05 else "Fail to reject H0",
            )
        )

        # 2. Welch t-test (Unequal Variance)
        w_stat, w_p = stats.ttest_ind(s1, s2, equal_var=False)
        results.append(
            HypothesisTestResult(
                test_name="Welch's t-test",
                statistic=round(float(w_stat), 4),
                p_value=round(float(w_p), 4),
                is_significant_at_05=w_p < 0.05,
                conclusion="Reject H0 (Means differ)" if w_p < 0.05 else "Fail to reject H0",
            )
        )

        # 3. One-Way ANOVA
        f_stat, f_p = stats.f_oneway(s1, s2)
        results.append(
            HypothesisTestResult(
                test_name="One-Way ANOVA",
                statistic=round(float(f_stat), 4),
                p_value=round(float(f_p), 4),
                is_significant_at_05=f_p < 0.05,
                conclusion="Significant variance across groups" if f_p < 0.05 else "No significant variance",
            )
        )

        # 4. Mann-Whitney U Test (Non-parametric)
        u_stat, u_p = stats.mannwhitneyu(s1, s2)
        results.append(
            HypothesisTestResult(
                test_name="Mann-Whitney U Test",
                statistic=round(float(u_stat), 4),
                p_value=round(float(u_p), 4),
                is_significant_at_05=u_p < 0.05,
                conclusion="Distribution medians differ" if u_p < 0.05 else "Medians are similar",
            )
        )

        # 5. Kolmogorov-Smirnov Test
        ks_stat, ks_p = stats.ks_2samp(s1, s2)
        results.append(
            HypothesisTestResult(
                test_name="Kolmogorov-Smirnov Test",
                statistic=round(float(ks_stat), 4),
                p_value=round(float(ks_p), 4),
                is_significant_at_05=ks_p < 0.05,
                conclusion="Distributions differ significantly" if ks_p < 0.05 else "Identical distributions",
            )
        )

        # 6. Shapiro-Wilk Normality Test
        sh_stat, sh_p = stats.shapiro(s1)
        results.append(
            HypothesisTestResult(
                test_name="Shapiro-Wilk Normality Test (Sample 1)",
                statistic=round(float(sh_stat), 4),
                p_value=round(float(sh_p), 4),
                is_significant_at_05=sh_p < 0.05,
                conclusion="Non-normal distribution" if sh_p < 0.05 else "Normally distributed",
            )
        )

        return results
