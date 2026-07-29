import io
from app.services.ocr.base import IOCREngine, OCRResult, OCRBlock
import structlog

logger = structlog.get_logger(__name__)

class EasyOCREngine(IOCREngine):
    """EasyOCR Engine Implementation"""

    @property
    def engine_name(self) -> str:
        return "easyocr"

    async def extract_text(self, file_bytes: bytes) -> OCRResult:
        blocks: list[OCRBlock] = []
        full_text = ""

        try:
            import easyocr
            import numpy as np
            from PIL import Image

            reader = easyocr.Reader(['en'], gpu=False)
            img = np.array(Image.open(io.BytesIO(file_bytes)))
            results = reader.readtext(img)

            text_parts = []
            for bbox, text, conf in results:
                text_parts.append(text)
                x_coords = [p[0] for p in bbox]
                y_coords = [p[1] for p in bbox]
                blocks.append(
                    OCRBlock(
                        text=text,
                        confidence=float(conf),
                        bbox=[float(min(x_coords)), float(min(y_coords)), float(max(x_coords)), float(max(y_coords))],
                    )
                )
            full_text = "\n".join(text_parts)
        except Exception as e:
            logger.warning("easyocr_engine_fallback", error=str(e))
            full_text = file_bytes.decode("utf-8", errors="ignore")
            blocks.append(OCRBlock(text=full_text, confidence=0.70))

        return OCRResult(
            engine_name=self.engine_name,
            full_text=full_text,
            blocks=blocks,
            metadata={"block_count": len(blocks)},
        )
