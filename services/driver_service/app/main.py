from fastapi import FastAPI

from services.driver_service.app.routes.driver_routes import router as driver_router


app = FastAPI(
    title="Driver Service"
)


app.include_router(driver_router)


@app.get("/health")
def health_check():
    return {"status": "Driver Service is running"}