from pydantic import BaseModel


class MatchRequest(BaseModel):
    ride_id: int
    rider_id: int
    pickup_lat: float
    pickup_lng: float


class MatchResponse(BaseModel):
    ride_id: int
    driver_id: int
    message: str