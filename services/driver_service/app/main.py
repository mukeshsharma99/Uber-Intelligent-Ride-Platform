from fastapi import FastAPI

from services.auth_service.app.database import Base, engine
from services.auth_service.app.models.user import User
from services.driver_service.app.models.driver_model import Driver


Base.metadata.create_all(bind=engine)

app = FastAPI()