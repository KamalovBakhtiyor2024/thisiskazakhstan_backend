from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, RegisterUser, Signin, GetProfileById

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('register_user/', RegisterUser.as_view()),
  path('signin/', Signin.as_view()),
  path('get_profile/', GetProfileById.as_view())
]
