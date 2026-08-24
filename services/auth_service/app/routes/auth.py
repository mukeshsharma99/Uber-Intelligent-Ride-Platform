from fastapi import APIRouter

from services.auth_service.app.models.user import User
from services.auth_service.app.utils.security import hash_password


auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@auth_router.post("/register")
def register_user(user: User):
    hashed_password = hash_password(user.password)

    return {
        "username": user.username,
        "email": user.email,
        "password_hash": hashed_password
    }