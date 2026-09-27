from fastapi import FastAPI

from app.routes.ride_routes import router as ride_router

from app.database import Base, engine
from app.models.ride import Ride

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ride Service",
    description="Ride management service for Uber Intelligent Ride Platform",
    version="1.0.0"
)

app.include_router(ride_router)


@app.get("/")
def home():
    return {"message": "Ride Service is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}