from fastapi import APIRouter, HTTPException

from app.schema import MatchRequest, MatchResponse
from app.services.matching_service import find_driver


router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "matching-service",
    }


@router.post("/match", response_model=MatchResponse)
def match_driver(request: MatchRequest):

    driver = find_driver()

    if not driver:
        raise HTTPException(
            status_code=404,
            detail="No available driver found",
        )

    return {
        "ride_id": request.ride_id,
        "driver_id": driver["id"],
        "message": "Driver matched successfully",
    }