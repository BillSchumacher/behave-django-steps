from dynamic_rest.viewsets import DynamicModelViewSet

from test_app.serializers.dynamic import RelatedModelSerializer, SimpleModelSerializer


class SimpleViewSet(DynamicModelViewSet):
    """SimpleModel viewset class."""

    serializer_class = SimpleModelSerializer


class RelatedViewSet(DynamicModelViewSet):
    """RelatedModel viewset class."""

    serializer_class = RelatedModelSerializer
