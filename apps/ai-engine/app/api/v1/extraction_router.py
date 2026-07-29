from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.extractor.question_extractor import QuestionExtractorService
from app.services.extractor.schema import ExtractedQuestion

router = APIRouter(prefix="/extraction", tags=["Question Extraction"])
extractor_service = QuestionExtractorService()

class ExtractRequest(BaseModel):
    raw_text: str

class ExtractResponse(BaseModel):
    extracted_count: int
    questions: List[ExtractedQuestion]

@router.post("/extract", response_model=ExtractResponse)
async def extract_questions(payload: ExtractRequest):
    """
    Asynchronously parses document text into question items preserving LaTeX equations,
    tables, diagram references, numerical units, and MCQ options.
    """
    try:
        questions = await extractor_service.extract_questions(payload.raw_text)
        return ExtractResponse(extracted_count=len(questions), questions=questions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Question extraction failed: {str(e)}")
