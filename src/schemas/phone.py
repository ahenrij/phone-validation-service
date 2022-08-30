"""Schemas (DTO) for phone model."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator


# Shared properties
class PhoneBase(BaseModel):
    """Phone Base Schema."""

    phone_number: Optional[str] = None
    confirmation_token: Optional[str] = None
    verified: Optional[bool] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    @validator("updated_at")
    def set_updated_at(cls, v):
        """Update field timestamp."""
        v = datetime.now()
        return v


# Properties to receive on item creation
class PhoneCreate(PhoneBase):
    """Phone Create Schema."""

    phone_number: str
    verified: bool = False


# Properties to receive on item update
class PhoneUpdate(PhoneBase):
    """Phone Update Schema."""


class PhoneInDBBase(PhoneBase):
    """Phone in database base schema."""

    id: str
    phone_number: str
    verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        """Config."""

        orm_mode = True


# Properties to return to client
class Phone(PhoneInDBBase):
    """Phone Schema."""
