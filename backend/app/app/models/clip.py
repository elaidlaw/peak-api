from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Clip(Base):
    id = Column(Integer, primary_key=True, index=True)
    link = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    camera_id = Column(Integer, ForeignKey("user.id"))
    timestamp = Column(DateTime)