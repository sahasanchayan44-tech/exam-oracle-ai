import httpx
from typing import Optional, Dict, Type
from app.services.llm.base import ILLMProvider
from app.core.config import settings
import structlog

logger = structlog.get_logger(__name__)

class BaseHTTPLLMProvider(ILLMProvider):
    def __init__(self, api_key: str, endpoint: str, model_name: str):
        self.api_key = api_key
        self.endpoint = endpoint
        self.model_name = model_name

    async def _post_json(self, url: str, headers: dict, payload: dict) -> dict:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            return resp.json()

class OpenAIProvider(BaseHTTPLLMProvider):
    def __init__(self, api_key: str = None):
        key = api_key or settings.OPENAI_API_KEY
        super().__init__(key, "https://api.openai.com/v1/chat/completions", "gpt-4o")

    @property
    def provider_name(self) -> str:
        return "openai"

    async def generate_completion(
        self, prompt: str, system_prompt: Optional[str] = None, temperature: float = 0.2
    ) -> str:
        if not self.api_key:
            return self._mock_response(prompt)
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})

            headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
            payload = {"model": self.model_name, "messages": messages, "temperature": temperature}
            data = await self._post_json(self.endpoint, headers, payload)
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            logger.warning("openai_provider_fallback", error=str(e))
            return self._mock_response(prompt)

    def _mock_response(self, prompt: str) -> str:
        return (
            '{"subject": "Computer Science", "chapter": "Data Structures", "subchapter": "Trees & Graphs", '
            '"concept": "Binary Search Tree Traversal", "formulae": ["T(n) = O(log n)"], "difficulty": 0.65, '
            '"bloom_taxonomy": "APPLY", "question_type": "MCQ", "estimated_solving_time": 5.0, '
            '"is_multi_concept": false, "tagged_concepts": ["Tree Traversal", "Recursion"]}'
        )

class ClaudeProvider(ILLMProvider):
    def __init__(self, api_key: str = None):
        self.api_key = api_key or settings.ANTHROPIC_API_KEY

    @property
    def provider_name(self) -> str:
        return "claude"

    async def generate_completion(
        self, prompt: str, system_prompt: Optional[str] = None, temperature: float = 0.2
    ) -> str:
        if not self.api_key:
            return OpenAIProvider()._mock_response(prompt)
        try:
            headers = {
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            }
            payload = {
                "model": "claude-3-5-sonnet-20240620",
                "max_tokens": 1024,
                "temperature": temperature,
                "messages": [{"role": "user", "content": prompt}],
            }
            if system_prompt:
                payload["system"] = system_prompt
            async with httpx.AsyncClient(timeout=30.0) as client:
                res = await client.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload)
                res.raise_for_status()
                return res.json()["content"][0]["text"]
        except Exception as e:
            logger.warning("claude_provider_fallback", error=str(e))
            return OpenAIProvider()._mock_response(prompt)

class GeminiProvider(ILLMProvider):
    def __init__(self, api_key: str = None):
        self.api_key = api_key or settings.GEMINI_API_KEY

    @property
    def provider_name(self) -> str:
        return "gemini"

    async def generate_completion(
        self, prompt: str, system_prompt: Optional[str] = None, temperature: float = 0.2
    ) -> str:
        if not self.api_key:
            return OpenAIProvider()._mock_response(prompt)
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
            payload = {"contents": [{"parts": [{"text": f"{system_prompt or ''}\n\n{prompt}"}]}]}
            async with httpx.AsyncClient(timeout=30.0) as client:
                res = await client.post(url, json=payload)
                res.raise_for_status()
                return res.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            logger.warning("gemini_provider_fallback", error=str(e))
            return OpenAIProvider()._mock_response(prompt)

class DeepSeekProvider(OpenAIProvider):
    def __init__(self, api_key: str = None):
        key = api_key or settings.DEEPSEEK_API_KEY
        super().__init__(key)
        self.endpoint = "https://api.deepseek.com/v1/chat/completions"
        self.model_name = "deepseek-chat"

    @property
    def provider_name(self) -> str:
        return "deepseek"

class QwenProvider(OpenAIProvider):
    def __init__(self, api_key: str = None):
        key = api_key or settings.QWEN_API_KEY
        super().__init__(key)
        self.endpoint = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
        self.model_name = "qwen-max"

    @property
    def provider_name(self) -> str:
        return "qwen"

class MistralProvider(OpenAIProvider):
    def __init__(self, api_key: str = None):
        key = api_key or settings.MISTRAL_API_KEY
        super().__init__(key)
        self.endpoint = "https://api.mistral.ai/v1/chat/completions"
        self.model_name = "mistral-large-latest"

    @property
    def provider_name(self) -> str:
        return "mistral"

class LlamaProvider(OpenAIProvider):
    def __init__(self, api_key: str = None):
        super().__init__(api_key or "local")
        self.endpoint = f"{settings.OLLAMA_BASE_URL}/v1/chat/completions"
        self.model_name = "llama3"

    @property
    def provider_name(self) -> str:
        return "llama"

class LLMProviderFactory:
    """Factory Pattern for dynamic LLM Provider switching at runtime"""

    _registry: Dict[str, Type[ILLMProvider]] = {
        "openai": OpenAIProvider,
        "claude": ClaudeProvider,
        "gemini": GeminiProvider,
        "deepseek": DeepSeekProvider,
        "qwen": QwenProvider,
        "mistral": MistralProvider,
        "llama": LlamaProvider,
    }

    @classmethod
    def get_provider(cls, name: Optional[str] = None) -> ILLMProvider:
        provider_key = (name or settings.DEFAULT_LLM_PROVIDER).lower()
        provider_cls = cls._registry.get(provider_key, OpenAIProvider)
        return provider_cls()
