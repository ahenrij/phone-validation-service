"""Main API v1"""

from fastapi import APIRouter

from src.api.v1.endpoints import model


api_router = APIRouter()

api_router.include_router(model.router, prefix="/phone", tags=["model"])
