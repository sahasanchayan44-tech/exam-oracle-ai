import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Exam Oracle AI Engine"
    API_V1_STR: str = "/api/v1"
    PORT: int = 8000
    LOG_LEVEL: str = "INFO"

    # Default LLM Provider Configuration
    DEFAULT_LLM_PROVIDER: str = os.getenv("DEFAULT_LLM_PROVIDER", "openai")

    # API Keys for Supported LLM Providers
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    MISTRAL_API_KEY: str = os.getenv("MISTRAL_API_KEY", "")
    QWEN_API_KEY: str = os.getenv("QWEN_API_KEY", "")
    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")

    # Ollama / Custom Local LLM Endpoint (Llama, DeepSeek, Qwen)
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    # Vector DB (Qdrant)
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", 6333))
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")
    QDRANT_COLLECTION: str = os.getenv("QDRANT_COLLECTION", "exam_questions")

    # Storage & DB
    MINIO_ENDPOINT: str = os.getenv("MINIO_ENDPOINT", "localhost:9000")
    MINIO_ACCESS_KEY: str = os.getenv("MINIO_ACCESS_KEY", "minio_admin_user")
    MINIO_SECRET_KEY: str = os.getenv("MINIO_SECRET_KEY", "minio_admin_password_2026")

    # NLP & Embeddings
    EMBEDDING_MODEL: str = os.getenv("AI_MODEL_TRANSFORMER", "sentence-transformers/all-mpnet-base-v2")

    # Non-Predictive Disclaimer Banner
    NON_PREDICTIVE_DISCLAIMER: str = (
        "Exam Oracle AI provides probabilistic estimations based on historical sample distributions. "
        "It DOES NOT predict exact future examination questions or papers."
    )

    class Config:
        case_sensitive = True

settings = Settings()
