from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.generation.question_synthesizer import QuestionSynthesizerService, SynthesizedQuestionResult

router = APIRouter(prefix="/synthesis", tags=["Practice Question Synthesizer"])
synthesizer_service = QuestionSynthesizerService()

class SynthesizeRequest(BaseModel):
    topic_name: str
    seed_question_text: str
    target_marks: int = 5
    difficulty: float = 0.60
    provider: Optional[str] = "openai"

@router.post("/generate", response_model=SynthesizedQuestionResult)
async def generate_question(payload: SynthesizeRequest):
    """
    Generates a novel, statistically equivalent practice question with step-by-step solution,
    scoring rubric, and vector embedding cosine similarity score relative to the seed question.
    """
    try:
        return await synthesizer_service.synthesize_practice_question(
            topic_name=payload.topic_name,
            seed_question_text=payload.seed_question_text,
            target_marks=payload.target_marks,
            difficulty=payload.difficulty,
            provider_name=payload.provider,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Question synthesis failed: {str(e)}")
