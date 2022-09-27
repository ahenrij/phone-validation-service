"""Phone resource endpoints."""

from http import HTTPStatus
from typing import Any
from fastapi import APIRouter, HTTPException

from src.models.phone import Phone
from src import schemas, utils
from src.core.config import settings
from src.utils import twilio


router = APIRouter()


@router.post("/phone", response_model=schemas.Phone)
async def create(*, model_in: schemas.PhoneCreate) -> Any:
    """Create a new phone entry."""
    # Get existing phone number record
    phone = await Phone.find_one(Phone.phone_number == model_in.phone_number)

    # Return if phone is already verified
    if phone and phone.verified:
        return HTTPException(
            status_code=HTTPStatus.CONFLICT, detail="Phone number already used"
        )

    # Save phone if not existed
    if not phone:
        confirmation_token = utils.random_n_digits(settings.OTP_CODE_LEN)
        phone = Phone(
            phoneNumber=model_in.phone_number,
            confirmatiomToken=confirmation_token,
        )
        await Phone.insert_one(phone)

    # Send sms to phone number
    message = twilio.send(
        to=model_in.phone_number,
        body=f"Your confirmation code is {phone.confirmation_token}",
    )
    if not message:
        return HTTPException(
            status_code=HTTPStatus.SERVICE_UNAVAILABLE, detail="Sending SMS failed."
        )

    return phone
