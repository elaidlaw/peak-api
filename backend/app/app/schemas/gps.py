from typing import Optional

from pydantic import BaseModel, EmailStr
from datetime import datetime


# Shared properties
class GPSBase(BaseModel):
    longitude: float
    latitude: float
    timestamp: datetime

# Properties to receive via API on creation
class GPSCreate(GPSBase):
    pass

class GPSCreateMultiResponse(BaseModel):
    count: int

# Properties to receive via API on update
class GPSUpdate(GPSBase):
    pass

class GPSInDBBase(GPSBase):
    user_id: int
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class GPS(GPSInDBBase):
    pass


# Additional properties stored in DB
class GPSInDB(GPSInDBBase):
    pass
