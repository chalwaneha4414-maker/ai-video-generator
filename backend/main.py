from fastapi import FastAPI

app = FastAPI(
    title="AI Video Generator API",
    description="Backend API for AI Video Generation Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Video Generator Backend is running 🚀"
    }