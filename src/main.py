"""Main FastAPI entry point."""

import logging

import uvicorn
from fastapi import FastAPI

from src.api.v1.main import api_router
from src.core.config import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
