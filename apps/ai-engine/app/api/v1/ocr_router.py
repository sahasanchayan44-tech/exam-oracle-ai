from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
from app.services.ocr.ocr_service import OCRService
from app.services.ocr.base import OCRResult

router = APIRouter(prefix="/ocr", tags=["OCR Engine"])
ocr_service = OCRService()

@router.post("/process", response_model=OCRResult)
async def process_ocr(
    file: UploadFile = File(...),
    preferred_engine: Optional[str] = Form("tesseract"),
):
    """
    Asynchronously extracts text and bounding blocks from uploaded PDF/Image files.
    Supports engines: 'tesseract', 'paddleocr', 'easyocr' with automatic fallback.
    """
    try:
        content = await file.read()
        return await ocr_service.process_document(content, preferred_engine=preferred_engine)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR processing failed: {str(e)}")
