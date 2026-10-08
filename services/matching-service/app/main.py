from fastapi import FastAPI
from app.routes.routes import router

app = FastAPI(
    title="Matching Service",
    description="Driver matching service for Uber Intelligent Ride Platform",
    version="1.0.0"
)

app.include_router(router)