from fastapi import FastAPI

from services.auth_service.app.routes.health import health_router
from services.auth_service.app.routes.auth import auth_router

app = FastAPI()

app.include_router(health_router)
app.include_router(auth_router)

