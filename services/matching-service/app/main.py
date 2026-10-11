from fastapi import FastAPI
from app.routes.routes import router

app = FastAPI(
    title="Uber Matching Service"
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "matching-service"
    }