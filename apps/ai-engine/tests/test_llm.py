import pytest
from app.services.llm.providers import LLMProviderFactory
from app.services.llm.classifier import QuestionClassifierService

@pytest.mark.asyncio
async def test_llm_factory_and_classification():
    provider = LLMProviderFactory.get_provider("deepseek")
    assert provider.provider_name == "deepseek"

    classifier = QuestionClassifierService()
    result = await classifier.classify_question("Implement a Binary Search Tree", provider_name="openai")
    assert result.subject is not None
    assert result.bloom_taxonomy is not None
    assert 0.0 <= result.difficulty <= 1.0
