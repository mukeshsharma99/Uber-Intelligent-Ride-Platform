from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.database import Base


class Ride(Base):
    __tablename__ = "rides"

    id = Column(Integer, primary_key=True, index=True)

    rider_id = Column(Integer, nullable=False)
    driver_id = Column(Integer, nullable=True)

    pickup_location = Column(String, nullable=False)
    drop_location = Column(String, nullable=False)

    status = Column(String, default="REQUESTED", nullable=False)

    fare = Column(Float, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)