from abc import ABC, abstractmethod
from typing import Optional

class ILLMProvider(ABC):
    """Abstract Base Interface for LLM Providers (OpenAI, Claude, Gemini, Llama, Mistral, Qwen, DeepSeek)"""

    @property
    @abstractmethod
    def provider_name(self) -> str:
        pass

    @abstractmethod
    async def generate_completion(
        self, prompt: str, system_prompt: Optional[str] = None, temperature: float = 0.2
    ) -> str:
        """Sends prompt to the LLM backend and returns completion string"""
        pass
