import math
from typing import List, Dict, Any
from pydantic import BaseModel

class EngineeredFeatures(BaseModel):
    syntactic_complexity: float
    difficulty_index: float
    bloom_weight: float
    temporal_recency_weight: float
    combined_importance_score: float

class FeatureEngineeringService:
    """Feature Engineering for Question Complexity, Temporal Decay & Bloom Weighting"""

    BLOOM_WEIGHTS = {
        "REMEMBER": 1.0,
        "UNDERSTAND": 1.2,
        "APPLY": 1.5,
        "ANALYZE": 1.8,
        "EVALUATE": 2.0,
        "CREATE": 2.2,
    }

    async def compute_features(
        self, question_text: str, bloom_level: str, year: int, current_year: int = 2026
    ) -> EngineeredFeatures:
        # 1. Syntactic Complexity (Average sentence length & word complexity)
        words = question_text.split()
        num_words = max(len(words), 1)
        avg_word_length = sum(len(w) for w in words) / num_words
        syntactic_comp = min(1.0, (num_words / 50.0) * (avg_word_length / 6.0))

        # 2. Bloom Weight
        bloom_w = self.BLOOM_WEIGHTS.get(bloom_level.upper(), 1.2)

        # 3. Temporal Recency Decay (Exponential decay factor e^(-lambda * delta_years))
        delta_years = max(0, current_year - year)
        lambda_decay = 0.08
        recency_weight = math.exp(-lambda_decay * delta_years)

        # 4. Combined Importance Score
        combined_score = round(syntactic_comp * bloom_w * recency_weight, 4)

        return EngineeredFeatures(
            syntactic_complexity=round(syntactic_comp, 4),
            difficulty_index=round(min(1.0, syntactic_comp * 0.8 + 0.2), 4),
            bloom_weight=bloom_w,
            temporal_recency_weight=round(recency_weight, 4),
            combined_importance_score=combined_score,
        )
