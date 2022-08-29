"""Phone model module."""

from bson import ObjectId
from pydantic import BaseModel, Field

from src.models import PyObjectId


class Phone(BaseModel):
    """Phone model class."""

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    phone_number: str = Field(...)
    confirmation_token: str = Field(...)
    verified: bool = Field(...)
    created_at: str = Field(...)
    updated_at: str = Field(...)

    class Config:
        """Phone model config."""

        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
