from fastapi import FastAPI

from services.ride_service.app.database import Base, engine
from services.ride_service.app.models.ride import Ride
from services.ride_service.app.routes.ride_routes import router as ride_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ride Service")

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "Ride Service is running"}

app.include_router(ride_router)