from fastapi import APIRouter
from services.auth_service.app.models.user import User

router = APIRouter()


@router.post("/register")
def register_user(user: User):
    return {
        "message": "User registered successfully",
        "username": user.username,
        "email": user.email
    }