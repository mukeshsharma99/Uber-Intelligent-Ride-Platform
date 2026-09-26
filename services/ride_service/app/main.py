
from fastapi import FastAPI

app = FastAPI(
    title="Ride Service",
    description="Ride management service for Uber Intelligent Ride Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Ride Service is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}