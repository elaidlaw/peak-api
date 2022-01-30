from typing import Optional

from pydantic import BaseModel, EmailStr
from datetime import datetime


# Shared properties
class ClipBase(BaseModel):
    link: str
    user_id: int
    camera_id: int
    timestamp: datetime

class ClipGet(BaseModel):
    start_timestamp: datetime
    end_timestamp: datetime

# Properties to receive via API on creation
class ClipCreate(ClipBase):
    pass

# Properties to receive via API on update
class ClipUpdate(ClipBase):
    pass

class ClipInDBBase(ClipBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Clip(ClipInDBBase):
    pass


# Additional properties stored in DB
class ClipInDB(ClipInDBBase):
    pass
