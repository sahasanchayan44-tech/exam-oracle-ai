from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class OCRBlock(BaseModel):
    text: str
    confidence: float
    bbox: Optional[List[float]] = None  # [x_min, y_min, x_max, y_max]

class OCRResult(BaseModel):
    engine_name: str
    full_text: str
    blocks: List[OCRBlock]
    metadata: Dict[str, Any] = {}

class IOCREngine(ABC):
    """Abstract Base Class for OCR Engines (PaddleOCR, Tesseract, EasyOCR)"""

    @property
    @abstractmethod
    def engine_name(self) -> str:
        pass

    @abstractmethod
    async def extract_text(self, file_bytes: bytes) -> OCRResult:
        """Extracts text and bounding box metadata from image or PDF page bytes"""
        pass
