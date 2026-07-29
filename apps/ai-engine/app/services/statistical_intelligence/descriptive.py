import numpy as np
import scipy.stats as stats
from typing import List, Dict, Any, Tuple
from pydantic import BaseModel

class DescriptiveStatsResult(BaseModel):
    mean: float
    median: float
    mode: float
    variance: float
    std_dev: float
    covariance_matrix: List[List[float]]
    sample_size: int

class DescriptiveStatisticsEngine:
    """Computes descriptive statistical metrics over historical examination features"""

    @staticmethod
    def calculate_stats(data: List[float], second_dataset: List[float] = None) -> DescriptiveStatsResult:
        arr = np.array(data, dtype=float)
        if len(arr) == 0:
            arr = np.array([0.0])

        mean_val = float(np.mean(arr))
        median_val = float(np.median(arr))

        # Mode calculation
        mode_res = stats.mode(arr, keepdims=True)
        mode_val = float(mode_res.mode[0]) if len(mode_res.mode) > 0 else mean_val

        variance_val = float(np.var(arr, ddof=1)) if len(arr) > 1 else 0.0
        std_val = float(np.std(arr, ddof=1)) if len(arr) > 1 else 0.0

        # Covariance matrix calculation
        if second_dataset and len(second_dataset) == len(data):
            arr2 = np.array(second_dataset, dtype=float)
            cov_mat = np.cov(arr, arr2).tolist()
        else:
            cov_mat = [[variance_val]]

        return DescriptiveStatsResult(
            mean=round(mean_val, 4),
            median=round(median_val, 4),
            mode=round(mode_val, 4),
            variance=round(variance_val, 4),
            std_dev=round(std_val, 4),
            covariance_matrix=[[round(val, 4) for val in row] for row in cov_mat],
            sample_size=len(data),
        )
