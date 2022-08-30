"""Database Session Manager."""

from beanie import init_beanie
import motor.motor_asyncio

from src.core.config import settings
from src.db import models


async def init_db():
    """Initialize database session."""
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(database=client.db_name, document_models=models)
