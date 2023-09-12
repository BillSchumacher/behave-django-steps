from rest_framework.routers import DefaultRouter

from test_app.viewsets.drf import RelatedViewSet, SimpleViewSet

router = DefaultRouter()
router.register("simple", SimpleViewSet)
router.register("related", RelatedViewSet)
