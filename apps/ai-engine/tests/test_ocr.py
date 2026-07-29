import pytest
from app.services.ocr.ocr_service import OCRService

@pytest.mark.asyncio
async def test_ocr_service_fallback():
    service = OCRService()
    sample_bytes = b"Question 1: Explain Binary Trees."
    result = await service.process_document(sample_bytes, preferred_engine="tesseract")
    assert result.engine_name is not None
    assert "Question 1" in result.full_text
