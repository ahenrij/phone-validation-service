"""Test settings class."""
from src.core.config import Settings


def test_settings_load():
    """Test settings loading."""
    settings = Settings()
    assert isinstance(settings.PROJECT_NAME, str)
