from pydantic import BaseModel


class DriverProfileCreate(BaseModel):
    full_name: str
    phone: str
    vehicle_number: str
    vehicle_model: str



    