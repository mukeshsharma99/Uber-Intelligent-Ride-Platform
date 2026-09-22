from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from services.auth_service.app.database import SessionLocal
from services.auth_service.app.utils.auth import get_current_user

from services.driver_service.app.models.driver_model import Driver
from services.driver_service.app.schemas.driver_schema import (
    DriverCreate,
    DriverResponse,
)

router = APIRouter(
    prefix="/drivers",
    tags=["Drivers"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/profile", response_model=DriverResponse)
def create_driver_profile(
    driver: DriverCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role != "DRIVER":
        raise HTTPException(
            status_code=403,
            detail="Only drivers can create a driver profile"
        )

    existing_driver = db.query(Driver).filter(
        Driver.user_id == current_user.id
    ).first()

    if existing_driver:
        raise HTTPException(
            status_code=400,
            detail="Driver profile already exists"
        )

    new_driver = Driver(
        user_id=current_user.id,
        full_name=driver.full_name,
        phone=driver.phone
    )

    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)

    return new_driver


@router.get("/profile", response_model=DriverResponse)
def get_driver_profile(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role != "DRIVER":
        raise HTTPException(
            status_code=403,
            detail="Only drivers can access this profile"
        )

    driver = db.query(Driver).filter(
        Driver.user_id == current_user.id
    ).first()

    if not driver:
        raise HTTPException(
            status_code=404,
            detail="Driver profile not found"
        )

    return driver