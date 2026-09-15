from pydantic import BaseModel


class RiderCreate(BaseModel):
    full_name: str
    phone: str


class RiderResponse(BaseModel):
    id: int
    user_id: int
    full_name: str
    phone: str

    class Config:
        from_attributes = True