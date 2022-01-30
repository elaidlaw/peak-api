from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Camera(Base):
    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Integer)
    latitude = Column(Integer)
    name = Column(String)
