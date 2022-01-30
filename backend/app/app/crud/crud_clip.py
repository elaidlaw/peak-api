from typing import Any, Dict, Optional, Union, List
from datetime import date

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.clip import Clip
from app.schemas.clip import ClipCreate, ClipUpdate, ClipGet


class CRUDClip(CRUDBase[Clip, ClipCreate, ClipUpdate]):
    
    def get_clips_by_timestamp(self, db: Session, *, user_id: int, start_timestamp: date, end_timestamp: date) -> List[Clip]:
        clips = db.query(Clip) \
            .filter(Clip.timestamp >= start_timestamp) \
            .filter(Clip.timestamp <= end_timestamp).all()
        return clips



clip = CRUDClip(Clip)
