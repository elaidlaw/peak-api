from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from datetime import date

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email

router = APIRouter()


@router.get("/", response_model=List[schemas.Clip])
def get_clips(
    *,
    db: Session = Depends(deps.get_db),
    start_timestamp: date,
    end_timestamp: date,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get clips by timestamp.
    """
    clips = crud.clip.get_clips_by_timestamp(db, start_timestamp=start_timestamp, end_timestamp=end_timestamp, user_id=current_user.id)
    return clips

@router.post("/", response_model=schemas.Clip)
def create_clip(
    *,
    db: Session = Depends(deps.get_db),
    clip_in: schemas.ClipCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Create clip.
    """
    clip = crud.clip.create(db=db, obj_in=clip_in)
    return clip

@router.delete("/", response_model=schemas.Clip)
def create_clip(
    *,
    db: Session = Depends(deps.get_db),
    clip_id: int,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Delete clip.
    """
    clip = crud.clip.remove(db=db, id=clip_id)
    return clip