from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from services.auth_service.app.database import get_db
from services.auth_service.app.models.user import User
from services.auth_service.app.models.rider_model import Rider
from services.auth_service.app.utils.auth import get_current_user
from services.auth_service.app.schemas import RiderCreate, RiderResponse


rider_router = APIRouter(
    prefix="/riders",
    tags=["Riders"]
)


@rider_router.post("/profile", response_model=RiderResponse)
def create_rider_profile(
    rider: RiderCreate,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user)
):
    current_user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if current_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if current_user.role != "RIDER":
        raise HTTPException(
            status_code=403,
            detail="Only RIDER users can create a rider profile"
        )

    existing_rider = (
        db.query(Rider)
        .filter(Rider.user_id == current_user.id)
        .first()
    )

    if existing_rider:
        raise HTTPException(
            status_code=400,
            detail="Rider profile already exists"
        )

    new_rider = Rider(
        user_id=current_user.id,
        full_name=rider.full_name,
        phone=rider.phone
    )

    db.add(new_rider)
    db.commit()
    db.refresh(new_rider)

    return new_rider