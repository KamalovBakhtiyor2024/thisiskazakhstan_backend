from django.urls import path, include
from rest_framework import routers
from .views import EducationalInstitutionViewSet

router = routers.DefaultRouter()
router.register(r'educational_institutions', EducationalInstitutionViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
