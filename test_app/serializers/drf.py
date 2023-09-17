"""DRF Serializers for test_app."""
from rest_framework.serializers import ModelSerializer

from test_app.models import RelatedModel, SimpleModel


class SimpleModelSerializer(ModelSerializer):
    """SimpleModel serializer class."""

    class Meta:
        """Meta class."""

        model = SimpleModel
        fields = ("id", "name", "description", "created_at", "updated_at")


class RelatedModelSerializer(ModelSerializer):
    """RelatedModel serializer class."""

    class Meta:
        """Meta class."""

        model = RelatedModel
        fields = ("id", "simple", "owner", "properties")
