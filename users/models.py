from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(
    User, 
    blank=False, 
    null=False, 
    related_name="profile", 
    on_delete=models.CASCADE, 
    verbose_name="Пользователь"
  )
  phone = models.CharField(
    max_length=125, 
    blank=True, 
    null=True, 
    verbose_name="Телефон"
  )
  ROLE_CHOICES = [
    # Вместо user можно было бы написать Пользователь, а вместо director, Директор
    # Но для мультиязычности на сайте, лучше использовать определённый слаг для плагина i18n
    (1, "user"),
    (2, "director")
  ]
  role = models.IntegerField(
    choices=ROLE_CHOICES,
    default=1,
    blank=True,
    null=True,
    verbose_name="Роль"
  )
  educational_institution = models.ForeignKey(
    "educational_institutions.EducationalInstitution",
    blank=True, 
    null=True,
    on_delete=models.SET_NULL,
    verbose_name="Образовательное учреждение"
  )

  def __str__(self):
    return str(self.user)

  class Meta:
    verbose_name_plural = "Профили пользователей"
    db_table = "users_profiles"

