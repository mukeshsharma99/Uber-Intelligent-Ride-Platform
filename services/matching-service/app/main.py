from fastapi import FastAPI
from app.routes.routes import router


app = FastAPI(title="Matching Service")


app.include_router(router)