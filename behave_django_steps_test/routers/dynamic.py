"""Dynamic router for testing."""
from dynamic_rest.routers import DynamicRouter

from test_app.viewsets.dynamic import RelatedViewSet, SimpleViewSet

router = DynamicRouter()
router.register("simple", SimpleViewSet)
router.register("related", RelatedViewSet)
