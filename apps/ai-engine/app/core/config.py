import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Exam Oracle AI Engine"
    API_V1_STR: str = "/api/v1"
    PORT: int = 8000
    LOG_LEVEL: str = "INFO"

    # Vector DB
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", 6333))
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")

    # Storage & DB
    MINIO_ENDPOINT: str = os.getenv("MINIO_ENDPOINT", "localhost:9000")
    MINIO_ACCESS_KEY: str = os.getenv("MINIO_ACCESS_KEY", "minio_admin_user")
    MINIO_SECRET_KEY: str = os.getenv("MINIO_SECRET_KEY", "minio_admin_password_2026")

    # NLP & AI Models
    EMBEDDING_MODEL: str = os.getenv("AI_MODEL_TRANSFORMER", "sentence-transformers/all-mpnet-base-v2")

    # Non-Predictive Disclaimer Banner
    NON_PREDICTIVE_DISCLAIMER: str = (
        "Exam Oracle AI provides probabilistic estimations based on historical sample distributions. "
        "It DOES NOT predict exact future examination questions or papers."
    )

    class Config:
        case_sensitive = True

settings = Settings()
