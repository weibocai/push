from rest_framework.routers import DefaultRouter

from .views import QcPushViewSet

router = DefaultRouter()
router.register(r'push', QcPushViewSet)
