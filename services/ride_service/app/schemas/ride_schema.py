
from pydantic import BaseModel
from typing import Optional


class RideCreate(BaseModel):
    rider_id: int
    pickup_location: str
    drop_location: str


class RideResponse(BaseModel):
    id: int
    rider_id: int
    driver_id: Optional[int] = None
    pickup_location: str
    drop_location: str
    status: str

    class Config:
        from_attributes = True