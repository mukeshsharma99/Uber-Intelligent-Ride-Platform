
from fastapi import FastAPI

from app.database import Base, engine
from app.models.ride import Ride
from app.routes.ride_routes import router as ride_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(
    title="Ride Service",
    description="Ride management service for Uber Intelligent Ride Platform",
    version="1.0.0"
)

# Register ride routes
app.include_router(ride_router)


@app.get("/")
def home():
    return {
        "message": "Ride Service is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }