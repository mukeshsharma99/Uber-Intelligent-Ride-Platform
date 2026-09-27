
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.ride import Ride
from app.schemas.ride_schema import RideCreate


router = APIRouter(
    prefix="/rides",
    tags=["Rides"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_ride(
    ride: RideCreate,
    db: Session = Depends(get_db)
):
    new_ride = Ride(**ride.model_dump())

    db.add(new_ride)
    db.commit()
    db.refresh(new_ride)

    return new_ride