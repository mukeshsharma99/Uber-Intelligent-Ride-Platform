from fastapi import FastAPI
from services.auth_service.app.models.user import User

app = FastAPI()


@app.get("/health")
def health_check():
    return {"Name": "Status"}


@app.post("/user")
def create_user(user: User):
    return user