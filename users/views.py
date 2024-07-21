from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from educational_institutions.models import EducationalInstitution
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class GetProfileById(APIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    return Profile.objects.all()
  
  def get(self, request):
    id = request.GET.get("id")
    
    profile = Profile.objects.get(id=id)
    profile_serializer = ProfileSerializer(profile)
    
    # Получаем пользователя из запроса
    user = request.user
    
    # Удаляем старый токен
    try:
      token = Token.objects.get(user=user)
      token.delete()
    except Token.DoesNotExist:
      pass

    # Создаём новый токен и изменяем last_login
    token = Token.objects.create(user=user)
    user.last_login = timezone.now()
    user.save()
    
    return Response([
      {"id": id, "token": token.key},
      profile_serializer.data
    ], status=200)
  

class Signin(APIView):
  permissions_classes = [AllowAny]
  queryset = Profile.objects.all()
  
  def get(self, request):
    login = request.GET.get("login")
    password = request.GET.get("password")
    
    try:
      profile = Profile.objects.get(user__username=login)
      
      # Пройти аутентификацию
      user = authenticate(username=login, password=password)

      if user is not None:
        # Удаляем старый токен
        try:
          token = Token.objects.get(user=user)
          token.delete()
        except Token.DoesNotExist:
          pass

        # Создаём новый токен и изменяем last_login
        token = Token.objects.create(user=user)
        user.last_login = timezone.now()
        user.save()
        
        profile_serializer = ProfileSerializer(profile)
        
        return Response([
          {"id": profile.id, "token": token.key},
          profile_serializer.data
        ], status=200)
      else:
        return Response({"error": "Неверный пароль"}, status=400)
    except Profile.DoesNotExist: 
      return Response({"error": "Данного пользователя не существует"}, status=404)


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        first_stage = request.data.get("first_stage") # boolean
        login = request.data.get("login") # str
        password = request.data.get("password") # str
        first_name = request.data.get("first_name") # str
        last_name = request.data.get("last_name") # str
        email = request.data.get("email") # str
        phone = request.data.get("phone") # str
        educational_institution_id = request.data.get("educational_institution") # id
        
        # Проверяем существует ли пользователь с данным логином
        try:
          user = User.objects.get(username=login)
              
          return Response(
            {"message": "Данный пользователь существует, войдите в аккаунт"},
            status=409
          )
        except User.DoesNotExist:
          if not first_stage:
            if (
              phone is None
              or first_name is None
              or last_name is None
              or email is None
            ):
              return Response({"error": "Ошибка данных запроса"}, status=400)
            else:
              # Удаляем символ "+" из начала номера телефона, если он присутствует
              phone = phone[1:] if phone.startswith("+") else phone
              
              # Получаем образовательное учреждение
              try:
                educational_institution = EducationalInstitution.objects.get(
                  id=educational_institution_id
                )
              except EducationalInstitution.DoesNotExist:
                return Response({"error": "Ошибка данных запроса"}, status=400)
              
              # Создаём пользователя
              user = User.objects.create(
                username=login,
                password=make_password(password),
                email=email,
                first_name=first_name,
                last_name=last_name
              )
              
              # Создаём профиль пользователя
              Profile.objects.create(
                user=user,
                phone=phone,
                educational_institution=educational_institution,
                role=1
              )

              return Response({"message": "Пользователь успешно зарегистрирован"}, status=200)
          else:
            return Response(True, status=200)
