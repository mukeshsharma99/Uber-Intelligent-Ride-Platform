from fastapi import FastAPI

from services.auth_service.app.database import Base, engine

from services.auth_service.app.models.user import User
from services.auth_service.app.models.rider_model import Rider

from services.auth_service.app.routes.health import health_router
from services.auth_service.app.routes.auth import auth_router
from services.auth_service.app.routes.rider_routes import rider_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(rider_router)