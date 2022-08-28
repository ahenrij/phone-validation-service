"""Phone resource endpoints."""

from typing import Any
from fastapi import APIRouter


router = APIRouter()


@router.get("/hello", response_model=str)
def get_phones() -> Any:
    """Retrieve phone numbers list."""
    return "Hello world !"
