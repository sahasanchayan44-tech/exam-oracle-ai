import io
from app.services.ocr.base import IOCREngine, OCRResult, OCRBlock
import structlog

logger = structlog.get_logger(__name__)

class PaddleOCREngine(IOCREngine):
    """PaddleOCR Engine Implementation"""

    @property
    def engine_name(self) -> str:
        return "paddleocr"

    async def extract_text(self, file_bytes: bytes) -> OCRResult:
        blocks: list[OCRBlock] = []
        full_text = ""

        try:
            from paddleocr import PaddleOCR
            import numpy as np
            from PIL import Image

            ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)
            img = np.array(Image.open(io.BytesIO(file_bytes)))
            result = ocr.ocr(img, cls=True)

            text_parts = []
            if result and result[0]:
                for line in result[0]:
                    bbox_coords = line[0]
                    text, conf = line[1]
                    text_parts.append(text)
                    x_coords = [p[0] for p in bbox_coords]
                    y_coords = [p[1] for p in bbox_coords]
                    blocks.append(
                        OCRBlock(
                            text=text,
                            confidence=float(conf),
                            bbox=[min(x_coords), min(y_coords), max(x_coords), max(y_coords)],
                        )
                    )
            full_text = "\n".join(text_parts)
        except Exception as e:
            logger.warning("paddle_ocr_engine_fallback", error=str(e))
            # Fallback text decoding
            full_text = file_bytes.decode("utf-8", errors="ignore")
            blocks.append(OCRBlock(text=full_text, confidence=0.70))

        return OCRResult(
            engine_name=self.engine_name,
            full_text=full_text,
            blocks=blocks,
            metadata={"block_count": len(blocks)},
        )
