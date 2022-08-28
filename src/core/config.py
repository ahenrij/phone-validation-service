"""Settings."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Project settings from .env file.
    This class looks for defined environments variables named after its variables and load their values.
    The .env file is considered by default.

    Args:
        BaseSettings (pydantic.BaseSettings): Base settings to override

    Raises
        ValueError: if something is wrong with .env file
    """

    PROJECT_NAME: str

    class Config:
        """Settings configs."""

        case_sensitive = True
        env_file = ".env"


settings = Settings()