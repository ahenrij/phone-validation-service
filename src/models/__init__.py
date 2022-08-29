"""Models module."""

from bson import ObjectId


class PyObjectId(ObjectId):
    """PyObjectId class."""

    @classmethod
    def __get_validators__(cls):
        """Get validators."""
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """Validate value."""
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object id.")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        """Update schema."""
        field_schema.update(type="string")
