from pydantic import BaseModel


class DriverCreate(BaseModel):
    full_name: str
    phone: str


class DriverResponse(BaseModel):
    id: int
    user_id: int
    full_name: str
    phone: str

    class Config:
        from_attributes = True