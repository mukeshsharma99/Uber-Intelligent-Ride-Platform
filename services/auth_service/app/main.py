from fastapi import FastAPI

from services.auth_service.app.database import Base, engine
from services.auth_service.app.models.user import User
from services.auth_service.app.models.rider_model import Rider

from services.auth_service.app.routes.health import health_router as health_routes
from services.auth_service.app.routes.auth import auth_router as authentication_routes
from services.auth_service.app.routes.rider_routes import rider_router as rider_routes


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Authentication Service")

app.include_router(health_routes)
app.include_router(authentication_routes)
app.include_router(rider_routes)