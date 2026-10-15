from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import jobs


app = FastAPI(
    title="AI Career Recommendation API",
    description="AI-Powered Resume Analyzer and Career Recommendation System",
    version="2.0.0"
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",

        "http://localhost:5174",
        "http://127.0.0.1:5174",

        "http://localhost:5175",
        "http://127.0.0.1:5175"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


app.include_router(jobs.router)


@app.get("/")
def home():

    return {
        "status": "success",
        "message": "AI Career Recommendation Backend Running",
        "version": "2.0.0"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "message": "Backend is running successfully"
    }


@app.on_event("startup")
async def startup_event():

    print("=" * 60)

    print("AI CAREER RECOMMENDATION API")

    print("=" * 60)

    print("FastAPI application started")

    print("Backend:")
    print("http://127.0.0.1:8000")

    print()

    print("Swagger:")
    print("http://127.0.0.1:8000/docs")

    print()

    print("Available endpoints:")

    print("GET  /")
    print("GET  /health")

    print("POST /upload-resume")
    print("POST /match-job")
    print("POST /skill-gap")
    print("POST /recommend-career")
    print("POST /resume-feedback")
    print("POST /learning-recommendations")
    print("POST /analyze-resume")

    print("=" * 60)