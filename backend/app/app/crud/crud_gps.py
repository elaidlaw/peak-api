from typing import Any, Dict, Optional, Union, List
from datetime import date

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import insert
from app.crud.base import CRUDBase
from app.models.gps import GPS
from app.schemas.gps import GPSCreate, GPSUpdate, GPSCreateMultiResponse


class CRUDGPS(CRUDBase[GPS, GPSCreate, GPSUpdate]):
    
    def create_multi(self, db: Session, *, user_id: int, objs_in: List[GPSCreate]) -> GPSCreateMultiResponse:
        obj_in_data = jsonable_encoder(objs_in)
        for obj in obj_in_data:
            obj["user_id"] = user_id
        stmt = insert(self.model).values(obj_in_data).returning(self.model.id)
        res = db.execute(stmt).columns("id")
        db.commit()
        return GPSCreateMultiResponse(
            count=res.rowcount
        )

gps = CRUDGPS(GPS)
