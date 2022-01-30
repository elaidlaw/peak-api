from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email

router = APIRouter()

@router.post("/", response_model=schemas.GPSCreateMultiResponse)
def create_gps(
    *,
    db: Session = Depends(deps.get_db),
    gps_in: List[schemas.GPSCreate],
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new GPS objects.
    """
    user = crud.gps.create_multi(db, user_id=current_user.id, obj_in=gps_in)
    return user