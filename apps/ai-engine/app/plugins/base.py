from abc import ABC, abstractmethod
from typing import List, Dict, Any
from pydantic import BaseModel

class ParsedQuestionDTO(BaseModel):
    question_number: int
    content: str
    marks: int
    sub_questions: List[Dict[str, Any]] = []

class TopicProbabilityDTO(BaseModel):
    topic_id: str
    topic_name: str
    estimated_probability: float  # [0.0 - 1.0]
    confidence_lower_bound: float
    confidence_upper_bound: float
    confidence_score: float  # [0.0 - 1.0]
    rationale: Dict[str, Any]

class SynthesizedQuestionDTO(BaseModel):
    topic_id: str
    question_text: str
    solution: str
    rubric: Dict[str, Any]
    marks: int
    similarity_score: float
    confidence_score: float

class IPaperParserPlugin(ABC):
    """Interface for modular examination paper parser plugins (PDF, DOCX, LaTeX, Scanned Image OCR)"""

    @property
    @abstractmethod
    def plugin_name(self) -> str:
        pass

    @property
    @abstractmethod
    def supported_mime_types(self) -> List[str]:
        pass

    @abstractmethod
    async def parse_paper(self, file_bytes: bytes, metadata: Dict[str, Any]) -> List[ParsedQuestionDTO]:
        """Parses raw exam document into structured question items"""
        pass

class IProbabilityEnginePlugin(ABC):
    """Interface for modular statistical/Bayesian probability estimation algorithms"""

    @property
    @abstractmethod
    def algorithm_id(self) -> str:
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        pass

    @abstractmethod
    async def estimate_distributions(
        self,
        historical_questions: List[Dict[str, Any]],
        topics: List[Dict[str, Any]],
        parameters: Dict[str, Any],
    ) -> List[TopicProbabilityDTO]:
        """Calculates probability distributions and confidence scores for topic occurrence"""
        pass

class IQuestionSynthesizerPlugin(ABC):
    """Interface for modular practice question generation plugins"""

    @property
    @abstractmethod
    def synthesizer_id(self) -> str:
        pass

    @abstractmethod
    async def synthesize_question(
        self,
        target_topic: Dict[str, Any],
        seed_question: Dict[str, Any],
        target_marks: int,
        difficulty: float,
    ) -> SynthesizedQuestionDTO:
        """Generates statistically similar practice question with rationale"""
        pass
