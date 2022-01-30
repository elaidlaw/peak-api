from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

# if TYPE_CHECKING:
#     from .item import Item  # noqa: F401


# class User(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     full_name = Column(String, index=True)
#     email = Column(String, unique=True, index=True, nullable=False)
#     hashed_password = Column(String, nullable=False)
#     is_active = Column(Boolean(), default=True)
#     is_superuser = Column(Boolean(), default=False)
#     items = relationship("Item", back_populates="owner")

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    is_superuser = Column(Boolean(), default=False)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    # link to reference photo
    profile_pic = Column(String)

class Follower(Base):
    id = Column(Integer, primary_key=True, index=True)
    from_id = Column(Integer, ForeignKey("user.id"))
    to_id = Column(Integer, ForeignKey("user.id"))
