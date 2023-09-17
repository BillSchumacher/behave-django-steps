"""DRF viewsets for test_app."""

from rest_framework.viewsets import ModelViewSet

from test_app.models import RelatedModel, SimpleModel
from test_app.serializers.drf import RelatedModelSerializer, SimpleModelSerializer


class SimpleViewSet(ModelViewSet):
    """SimpleModel viewset class."""

    queryset = SimpleModel.objects.all()
    serializer_class = SimpleModelSerializer


class RelatedViewSet(ModelViewSet):
    """RelatedModel viewset class."""

    queryset = RelatedModel.objects.all()
    serializer_class = RelatedModelSerializer
