
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.ride import Ride
from app.schemas.ride_schema import RideCreate, RideStatusUpdate

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


# Create a new ride
@router.post("/")
def create_ride(
    ride_data: RideCreate,
    db: Session = Depends(get_db)
):
    new_ride = Ride(**ride_data.model_dump())

    db.add(new_ride)
    db.commit()
    db.refresh(new_ride)

    return new_ride


# Get all rides
@router.get("/")
def get_all_rides(
    db: Session = Depends(get_db)
):
    return db.query(Ride).all()


# Get ride by ID
@router.get("/{ride_id}")
def get_ride_by_id(
    ride_id: int,
    db: Session = Depends(get_db)
):
    ride = db.query(Ride).filter(
        Ride.id == ride_id
    ).first()

    if ride is None:
        raise HTTPException(
            status_code=404,
            detail="Ride not found"
        )

    return ride


# Update ride status
@router.patch("/{ride_id}/status")
def update_ride_status(
    ride_id: int,
    status_data: RideStatusUpdate,
    db: Session = Depends(get_db)
):
    ride = db.query(Ride).filter(
        Ride.id == ride_id
    ).first()

    if ride is None:
        raise HTTPException(
            status_code=404,
            detail="Ride not found"
        )

    ride.status = status_data.status

    db.commit()
    db.refresh(ride)

    return ride