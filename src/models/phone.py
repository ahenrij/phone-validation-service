"""Phone model module."""

from datetime import datetime
from beanie import Document
from pydantic import Field


class Phone(Document):
    """Phone model class."""

    phone_number: str = Field(..., alias="phoneNumber", allow_mutation=False)
    confirmation_token: str = Field(..., alias="confirmationToken")
    verified: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now(), alias="createdAt")
    updated_at: datetime = Field(default=datetime.now(), alias="updatedAt")

    class Config:
        """Phone model config."""

        schema_extra = {
            "example": {
                "phone_number": "33 6 00 00 00 00",
                "verified": False,
                "confirmation_token": None,
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            }
        }
