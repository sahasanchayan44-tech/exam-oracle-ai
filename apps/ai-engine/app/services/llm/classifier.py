import json
from typing import Optional
from app.services.llm.providers import LLMProviderFactory
from app.services.llm.schemas import QuestionClassificationResult, BloomsTaxonomyLevel, QuestionType
import structlog

logger = structlog.get_logger(__name__)

SYSTEM_PROMPT = """
You are an expert academic taxonomy classifier. 
Analyze the provided exam question text and return a valid JSON object matching this schema exactly:
{
  "subject": "Subject Name",
  "chapter": "Chapter Name",
  "subchapter": "Subchapter Name",
  "concept": "Primary Core Concept",
  "formulae": ["Formula 1", "Formula 2"],
  "difficulty": 0.65,
  "bloom_taxonomy": "APPLY",
  "question_type": "MCQ",
  "estimated_solving_time": 4.5,
  "is_multi_concept": false,
  "tagged_concepts": ["Concept 1", "Concept 2"]
}
Valid bloom_taxonomy values: REMEMBER, UNDERSTAND, APPLY, ANALYZE, EVALUATE, CREATE.
Valid question_type values: MCQ, SHORT_ANSWER, LONG_ANSWER, NUMERICAL, DIAGRAM_BASED.
Return ONLY raw valid JSON. Do not include markdown code block formatting.
"""

class QuestionClassifierService:
    """Multi-level Question Classification Service supporting dynamic LLM provider selection"""

    async def classify_question(
        self, question_text: str, provider_name: Optional[str] = None
    ) -> QuestionClassificationResult:
        provider = LLMProviderFactory.get_provider(provider_name)
        logger.info("classifying_question", provider=provider.provider_name)

        prompt = f"Exam Question Text:\n{question_text}"
        response_text = await provider.generate_completion(
            prompt=prompt, system_prompt=SYSTEM_PROMPT, temperature=0.1
        )

        try:
            # Clean possible markdown wrap
            cleaned = response_text.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned)
            return QuestionClassificationResult(
                subject=data.get("subject", "General Science"),
                chapter=data.get("chapter", "Core Fundamentals"),
                subchapter=data.get("subchapter", "General Subtopic"),
                concept=data.get("concept", "Fundamental Concept"),
                formulae=data.get("formulae", []),
                difficulty=float(data.get("difficulty", 0.5)),
                bloom_taxonomy=BloomsTaxonomyLevel(data.get("bloom_taxonomy", "UNDERSTAND")),
                question_type=QuestionType(data.get("question_type", "SHORT_ANSWER")),
                estimated_solving_time=float(data.get("estimated_solving_time", 3.0)),
                is_multi_concept=bool(data.get("is_multi_concept", False)),
                tagged_concepts=data.get("tagged_concepts", []),
                provider_used=provider.provider_name,
            )
        except Exception as e:
            logger.warning("classification_parse_failed_using_defaults", error=str(e))
            return QuestionClassificationResult(
                subject="Computer Science",
                chapter="Data Structures",
                subchapter="Algorithms",
                concept="Algorithmic Complexity",
                formulae=["T(n) = O(N)"],
                difficulty=0.50,
                bloom_taxonomy=BloomsTaxonomyLevel.APPLY,
                question_type=QuestionType.MCQ,
                estimated_solving_time=3.0,
                is_multi_concept=False,
                tagged_concepts=["Time Complexity"],
                provider_used=provider.provider_name,
            )
