"""App configuration for test_app."""
from django.apps import AppConfig


class TestAppConfig(AppConfig):
    """App configuration for test_app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "test_app"
