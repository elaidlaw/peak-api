from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class GPS(Base):
    id = Column(Integer, primary_key=True, index=True)
    # first_name = Column(String, index=True)
    # last_name = Column(String, index=True)
    # email = Column(String, unique=True, index=True, nullable=False)
    # hashed_password = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    longitude = Column(Integer)
    latitude = Column(Integer)
    timestamp = Column(DateTime)
