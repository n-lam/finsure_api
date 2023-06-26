from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LenderViewSet

router = DefaultRouter()
router.register(r"lenders", LenderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
