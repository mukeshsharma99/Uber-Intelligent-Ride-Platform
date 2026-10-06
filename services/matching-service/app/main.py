from fastapi import FastAPI

app = FastAPI(
    title="Matching Service",
    description="Driver matching service for Uber Intelligent Ride Platform",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "matching-service"
    }