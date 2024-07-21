from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import EducationalInstitution
from .serializers import EducationalInstitutionSerializer

# Create your views here.
class EducationalInstitutionViewSet(viewsets.ModelViewSet):
    queryset = EducationalInstitution.objects.all()
    serializer_class = EducationalInstitutionSerializer
    permission_classes = [AllowAny]
