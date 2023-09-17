"""Dynamic serializers for test_app."""

from django.contrib.auth import get_user_model
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

from test_app.models import RelatedModel, SimpleModel

User = get_user_model()


class SimpleModelSerializer(DynamicModelSerializer):
    """SimpleModel serializer class."""

    class Meta:
        """Meta class."""

        model = SimpleModel
        fields = ("id", "name", "description", "created_at", "updated_at")


class UserSerializer(DynamicModelSerializer):
    """User serializer class."""

    class Meta:
        """Meta class."""

        model = User
        fields = ("id", "username")


class RelatedModelSerializer(DynamicModelSerializer):
    """RelatedModel serializer class."""

    simple = DynamicRelationField(SimpleModelSerializer, embed=True)
    owner = DynamicRelationField(UserSerializer, embed=False)

    class Meta:
        """Meta class."""

        model = RelatedModel
        fields = ("id", "simple", "owner", "properties")
