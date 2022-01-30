from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class GPS(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    longitude = Column(Float)
    latitude = Column(Float)
    timestamp = Column(DateTime)
