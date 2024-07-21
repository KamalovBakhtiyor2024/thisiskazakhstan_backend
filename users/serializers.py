from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from educational_institutions.serializers import EducationalInstitutionSerializer

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
  user = UserSerializer(required=True)
  educational_institution = EducationalInstitutionSerializer()
  
  class Meta:
    model = Profile
    fields = [
      "user",
      "phone",
      "role",
      "educational_institution"
    ]
