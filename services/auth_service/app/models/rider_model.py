from sqlalchemy import Column, Integer, String, ForeignKey
from services.auth_service.app.database import Base


class Rider(Base):
    __tablename__ = "riders"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)