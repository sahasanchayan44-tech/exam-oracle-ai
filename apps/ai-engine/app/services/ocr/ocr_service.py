from typing import Dict, Optional
from app.services.ocr.base import IOCREngine, OCRResult
from app.services.ocr.tesseract_engine import TesseractOCREngine
from app.services.ocr.paddle_engine import PaddleOCREngine
from app.services.ocr.easyocr_engine import EasyOCREngine
import structlog

logger = structlog.get_logger(__name__)

class OCRService:
    """Unified OCR Manager with dynamic engine selection and fallback resilience"""

    def __init__(self):
        self._engines: Dict[str, IOCREngine] = {
            "tesseract": TesseractOCREngine(),
            "paddleocr": PaddleOCREngine(),
            "easyocr": EasyOCREngine(),
        }

    def register_engine(self, engine: IOCREngine):
        self._engines[engine.engine_name.lower()] = engine

    async def process_document(
        self, file_bytes: bytes, preferred_engine: Optional[str] = "tesseract"
    ) -> OCRResult:
        engine_key = (preferred_engine or "tesseract").lower()

        if engine_key in self._engines:
            try:
                logger.info("executing_ocr_engine", engine=engine_key)
                return await self._engines[engine_key].extract_text(file_bytes)
            except Exception as e:
                logger.warning("primary_ocr_engine_failed", engine=engine_key, error=str(e))

        # Fallback chain across available engines
        for name, engine in self._engines.items():
            if name != engine_key:
                try:
                    logger.info("fallback_ocr_engine_attempt", engine=name)
                    return await engine.extract_text(file_bytes)
                except Exception as ex:
                    logger.warning("fallback_ocr_engine_failed", engine=name, error=str(ex))

        # Absolute default string decoding
        full_text = file_bytes.decode("utf-8", errors="ignore")
        return OCRResult(
            engine_name="raw_fallback",
            full_text=full_text,
            blocks=[],
            metadata={"status": "degraded_raw_text"},
        )
