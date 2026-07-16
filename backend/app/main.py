from fastapi import FastAPI
from app.api.routes import health
from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API for AI Video Generation Platform",
    version=settings.APP_VERSION
)


app.include_router(
    health.router,
    prefix="/api",
    tags=["Health"]
)


@app.get("/")
def home():
    return {
        "message": "AI Video Generator Backend is running 🚀",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }