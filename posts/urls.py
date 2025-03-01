from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
