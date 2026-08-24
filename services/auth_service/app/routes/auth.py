from fastapi import APIRouter
from services.auth_service.app.models.user import User

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@auth_router.post("/register")
def register_user(user: User):
    return user