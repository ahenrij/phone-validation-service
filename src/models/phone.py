"""Phone model module."""

from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import Field

from src.db import Base


class Phone(Base):
    """Phone model class."""

    phone_number: str = Field(..., alias="phoneNumber", allow_mutation=False)
    confirmation_token: Optional[str] = Field(..., alias="confirmationToken")
    verified: bool = Field(...)
    created_at: datetime = Field(..., default=datetime.now(), alias="createdAt")
    updated_at: datetime = Field(..., default=datetime.now(), alias="updatedAt")

    class Config:
        """Phone model config."""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "phone_number": "33 6 00 00 00 00",
                "verified": False,
                "confirmation_token": None,
                "created_at": "",
                "updated_at": "",
            }
        }
