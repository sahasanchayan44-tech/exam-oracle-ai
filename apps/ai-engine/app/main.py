from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1.router import router as api_v1_router

setup_logging(settings.LOG_LEVEL)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description=(
        "Exam Oracle AI Engine - High Performance Statistical Analysis, NLP Feature Extraction, "
        "and Probabilistic Topic Distribution Modeling."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Exam Oracle AI Engine Service",
        "docs": f"{settings.API_V1_STR}/docs",
        "disclaimer": settings.NON_PREDICTIVE_DISCLAIMER,
    }
