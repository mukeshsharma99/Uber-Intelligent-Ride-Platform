from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.auth_service.app.database import SessionLocal
from services.auth_service.app.models.user import User
from services.auth_service.app.schemas.user import UserCreate
from services.auth_service.app.utils.security import hash_password


auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@auth_router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email
    }