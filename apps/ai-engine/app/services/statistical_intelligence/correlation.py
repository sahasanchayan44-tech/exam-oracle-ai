import numpy as np
import scipy.stats as stats
from typing import List, Dict, Any
from pydantic import BaseModel

class CorrelationResult(BaseModel):
    pearson_coefficient: float
    pearson_p_value: float
    spearman_coefficient: float
    spearman_p_value: float
    kendall_tau: float
    kendall_p_value: float
    partial_correlation: float

class CorrelationEngine:
    """Correlation analysis suite: Pearson, Spearman, Kendall Tau, & Partial Correlation"""

    @staticmethod
    def analyze_correlation(x: List[float], y: List[float], z_control: List[float] = None) -> CorrelationResult:
        arr_x = np.array(x, dtype=float)
        arr_y = np.array(y, dtype=float)

        if len(arr_x) < 2 or len(arr_y) < 2 or len(arr_x) != len(arr_y):
            return CorrelationResult(
                pearson_coefficient=0.0,
                pearson_p_value=1.0,
                spearman_coefficient=0.0,
                spearman_p_value=1.0,
                kendall_tau=0.0,
                kendall_p_value=1.0,
                partial_correlation=0.0,
            )

        # 1. Pearson
        r_p, p_p = stats.pearsonr(arr_x, arr_y)

        # 2. Spearman
        r_s, p_s = stats.spearmanr(arr_x, arr_y)

        # 3. Kendall Tau
        r_k, p_k = stats.kendalltau(arr_x, arr_y)

        # 4. Partial Correlation (controlling for z_control if provided)
        partial_corr = float(r_p)
        if z_control and len(z_control) == len(x):
            arr_z = np.array(z_control, dtype=float)
            r_xz, _ = stats.pearsonr(arr_x, arr_z)
            r_yz, _ = stats.pearsonr(arr_y, arr_z)
            denom = np.sqrt((1 - r_xz**2) * (1 - r_yz**2))
            if denom > 1e-9:
                partial_corr = float((r_p - r_xz * r_yz) / denom)

        return CorrelationResult(
            pearson_coefficient=round(float(r_p), 4),
            pearson_p_value=round(float(p_p), 4),
            spearman_coefficient=round(float(r_s), 4),
            spearman_p_value=round(float(p_s), 4),
            kendall_tau=round(float(r_k), 4),
            kendall_p_value=round(float(p_k), 4),
            partial_correlation=round(float(partial_corr), 4),
        )
