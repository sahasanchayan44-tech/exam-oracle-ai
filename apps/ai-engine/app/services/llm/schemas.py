from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum

class BloomsTaxonomyLevel(str, Enum):
    REMEMBER = "REMEMBER"
    UNDERSTAND = "UNDERSTAND"
    APPLY = "APPLY"
    ANALYZE = "ANALYZE"
    EVALUATE = "EVALUATE"
    CREATE = "CREATE"

class QuestionType(str, Enum):
    MCQ = "MCQ"
    SHORT_ANSWER = "SHORT_ANSWER"
    LONG_ANSWER = "LONG_ANSWER"
    NUMERICAL = "NUMERICAL"
    DIAGRAM_BASED = "DIAGRAM_BASED"

class QuestionClassificationResult(BaseModel):
    subject: str
    chapter: str
    subchapter: str
    concept: str
    formulae: List[str] = []
    difficulty: float = Field(..., ge=0.0, le=1.0)
    bloom_taxonomy: BloomsTaxonomyLevel
    question_type: QuestionType
    estimated_solving_time: float # Minutes
    is_multi_concept: bool = False
    tagged_concepts: List[str] = []
    provider_used: str = "openai"
