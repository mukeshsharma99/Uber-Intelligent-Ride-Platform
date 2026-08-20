from fastapi import FastAPI
from services.auth_service.app.routes.health import router as health_router

app = FastAPI()

app.include_router(health_router)