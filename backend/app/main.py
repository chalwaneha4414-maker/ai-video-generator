from fastapi import FastAPI
from app.api.routes import health, auth
from app.core.config import settings
from app.database.connection import engine
from app.database.base import Base


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

app.include_router(
    auth.router,
    prefix="/api/auth",
    tags=["Authentication"]
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "AI Video Generator Backend is running 🚀",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }