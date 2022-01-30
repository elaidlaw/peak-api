from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

# if TYPE_CHECKING:
#     from .user import User  # noqa: F401


class Photo(Base):
    id = Column(Integer, primary_key=True, index=True)
    link = Column(String)
    user_id = Column(Integer, ForeignKey("camera.id"))
    timestamp = Column(DateTime)