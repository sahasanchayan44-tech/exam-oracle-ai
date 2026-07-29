import io
from app.services.ocr.base import IOCREngine, OCRResult, OCRBlock
from app.core.logging import setup_logging
import structlog

logger = structlog.get_logger(__name__)

class TesseractOCREngine(IOCREngine):
    """Tesseract OCR Engine Implementation with graceful fallback"""

    @property
    def engine_name(self) -> str:
        return "tesseract"

    async def extract_text(self, file_bytes: bytes) -> OCRResult:
        blocks: list[OCRBlock] = []
        full_text = ""

        try:
            import pytesseract
            from PIL import Image

            image = Image.open(io.BytesIO(file_bytes))
            data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

            text_parts = []
            for i in range(len(data["text"])):
                text = data["text"][i].strip()
                conf = float(data["conf"][i]) if data["conf"][i] != "-1" else 0.0
                if text:
                    text_parts.append(text)
                    x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
                    blocks.append(
                        OCRBlock(
                            text=text,
                            confidence=conf / 100.0,
                            bbox=[float(x), float(y), float(x + w), float(y + h)],
                        )
                    )
            full_text = " ".join(text_parts)

        except Exception as e:
            logger.warning("tesseract_ocr_fallback_engaged", error=str(e))
            # Fallback text extraction if binary missing or unreadable
            try:
                import pypdf
                reader = pypdf.PdfReader(io.BytesIO(file_bytes))
                extracted_pages = [page.extract_text() or "" for page in reader.pages]
                full_text = "\n".join(extracted_pages)
                blocks.append(OCRBlock(text=full_text, confidence=0.85))
            except Exception:
                full_text = file_bytes.decode("utf-8", errors="ignore")
                blocks.append(OCRBlock(text=full_text, confidence=0.50))

        return OCRResult(
            engine_name=self.engine_name,
            full_text=full_text,
            blocks=blocks,
            metadata={"block_count": len(blocks)},
        )
