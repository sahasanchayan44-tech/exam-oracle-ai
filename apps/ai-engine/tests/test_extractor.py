import pytest
from app.services.extractor.question_extractor import QuestionExtractorService

@pytest.mark.asyncio
async def test_question_extraction_preserves_latex_and_options():
    extractor = QuestionExtractorService()
    raw = """
    Q1. Calculate the force $F = m \cdot a$ given $m = 10kg$ and $a = 9.8 m/s^2$. [5 marks]
    (A) 98 N
    (B) 49 N
    (C) 100 N
    (D) 10 N
    """
    questions = await extractor.extract_questions(raw)
    assert len(questions) == 1
    q = questions[0]
    assert q.question_number == 1
    assert len(q.equations) > 0
    assert len(q.options) == 4
    assert q.is_numerical is True
