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
    API_V1_STR: str = "/v1"
    DATABASE_TYPE: str
    DATABASE_URL: str
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_SENDER: str

    class Config:
        """Settings configs."""

        case_sensitive = True
        env_file = ".env"


settings = Settings()
