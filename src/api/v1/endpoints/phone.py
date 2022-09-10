"""Phone resource endpoints."""

from typing import Any
from fastapi import APIRouter

from src.models.phone import Phone
from src import schemas


router = APIRouter()


@router.post("/phone", response_model=schemas.Phone)
async def create(*, model_in: schemas.PhoneCreate) -> Any:
    """Create a new phone entry."""
    # Retrieve phone number
    phone = await Phone.find_one(Phone.phone_number == model_in.phone_number)

    return phone
