"""Database base class."""

from pydantic import BaseModel, Field

from src.db.utils import PyObjectId


class Base(BaseModel):
    """Models Base Class."""

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
