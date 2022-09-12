"""Phone resource endpoints."""

import math
import random
from typing import Any
from fastapi import APIRouter, HTTPException

from src.models.phone import Phone
from src import schemas


router = APIRouter()


@router.post("/phone", response_model=schemas.Phone)
async def create(*, model_in: schemas.PhoneCreate) -> Any:
    """Create a new phone entry."""
    # Retrieve phone number
    phone = await Phone.find_one(Phone.phone_number == model_in.phone_number)
    # Return if phone is already verified
    if phone and phone.verified:
        return HTTPException(status_code=409, detail="Phone number already used")

    if not phone:
        confirmation_token = math.floor(1000 + random.randint(0, 9) * 9000)  # noqa
        phone = Phone(
            phoneNumber=model_in.phone_number,
            confirmatiomToken=confirmation_token,
        )

    return phone
