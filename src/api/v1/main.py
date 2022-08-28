"""Main API v1"""

from fastapi import APIRouter

from src.api.v1.endpoints import phone


api_router = APIRouter()

api_router.include_router(phone.router, prefix="/phone", tags=["phone"])
