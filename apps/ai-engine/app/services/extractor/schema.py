from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ExtractedQuestion(BaseModel):
    question_number: int
    content: str
    marks: int = 1
    options: List[Dict[str, str]] = []  # [{"label": "A", "text": "Option text"}]
    equations: List[str] = []           # Extracted LaTeX formulas
    images: List[Dict[str, Any]] = []    # Extracted diagram/image references
    tables: List[Dict[str, Any]] = []    # Extracted table structures
    is_numerical: bool = False
    numerical_units: List[str] = []
    sub_questions: List[Dict[str, Any]] = []
    raw_snippet: str
