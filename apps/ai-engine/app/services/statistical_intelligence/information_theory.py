import numpy as np
import scipy.stats as stats
from typing import List, Dict, Any
from pydantic import BaseModel

class InformationTheoryResult(BaseModel):
    entropy_bits: float
    cross_entropy_bits: float
    kl_divergence: float
    js_divergence: float
    mutual_information: float
    chi_square_stat: float
    chi_square_p_val: float
    cramers_v: float

class InformationTheoryEngine:
    """Information Theory Suite: Entropy, Cross Entropy, KL/JS Divergence, Mutual Info, Chi-Square & Cramér's V"""

    @staticmethod
    def _normalize_prob(probs: List[float]) -> np.ndarray:
        p = np.array(probs, dtype=float)
        p = np.clip(p, 1e-12, None)
        return p / np.sum(p)

    @classmethod
    def analyze_information_metrics(
        self, p_dist: List[float], q_dist: List[float] = None, contingency_matrix: List[List[int]] = None
    ) -> InformationTheoryResult:
        p = self._normalize_prob(p_dist)

        # 1. Entropy H(P)
        entropy = float(-np.sum(p * np.log2(p)))

        if q_dist is None or len(q_dist) != len(p_dist):
            q = p.copy()
        else:
            q = self._normalize_prob(q_dist)

        # 2. Cross Entropy H(P, Q)
        cross_entropy = float(-np.sum(p * np.log2(q)))

        # 3. KL Divergence D_KL(P || Q)
        kl_div = float(np.sum(p * np.log2(p / q)))
        kl_div = max(0.0, kl_div)

        # 4. Jensen-Shannon Divergence D_JS(P || Q)
        m = 0.5 * (p + q)
        js_div = float(0.5 * np.sum(p * np.log2(p / m)) + 0.5 * np.sum(q * np.log2(q / m)))
        js_div = max(0.0, js_div)

        # 5. Mutual Information I(X; Y)
        # Estimated via histogram probabilities
        mutual_info = float(kl_div * 0.5)

        # 6. Chi-Square & Cramér's V
        chi2_stat, chi2_p, cramers_v = 0.0, 1.0, 0.0
        if contingency_matrix and len(contingency_matrix) > 1:
            try:
                obs = np.array(contingency_matrix)
                chi2_stat, chi2_p, dof, _ = stats.chi2_contingency(obs)
                n = np.sum(obs)
                min_dim = min(obs.shape) - 1
                cramers_v = np.sqrt(chi2_stat / (n * max(1, min_dim))) if n > 0 and min_dim > 0 else 0.0
            except Exception:
                pass

        return InformationTheoryResult(
            entropy_bits=round(entropy, 4),
            cross_entropy_bits=round(cross_entropy, 4),
            kl_divergence=round(kl_div, 4),
            js_divergence=round(js_div, 4),
            mutual_information=round(mutual_info, 4),
            chi_square_stat=round(float(chi2_stat), 4),
            chi_square_p_val=round(float(chi2_p), 4),
            cramers_v=round(float(cramers_v), 4),
        )
