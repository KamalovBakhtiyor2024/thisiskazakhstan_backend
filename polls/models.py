from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def background_image_path(instance, filename):
    return "user_{username}/{file}".format(username=instance.user.username, file=filename)

class CharField(models.Model):
  text = models.CharField(
    max_length=256,
    blank=True,
    null=True,
  )
  label = models.CharField(
    max_length=128,
    blank=False,
    null=False,
    verbose_name="Название поля"
  )
  
  def __str__(self):
    return str(self.label)

  class Meta:
    verbose_name_plural = "Charfields"


class CheckField(models.Model):
  status = models.BooleanField(
    default=False,
    verbose_name="Статус"
  )
  label = models.CharField(
    max_length=128,
    blank=False,
    null=False,
    verbose_name="Название поля"
  )
  
  def __str__(self):
    return str(self.label)

  class Meta:
    verbose_name_plural = "Checkfields"


class Poll(models.Model):
  user = models.ForeignKey(
    User,
    blank=False,
    null=False,
    on_delete=models.CASCADE,
    verbose_name="Пользователь"
  )
  LANG_CHOICES = [
    ("ru", "ru"),
    ("kz", "kz")
  ]
  lang = models.CharField(
    choices=LANG_CHOICES,
    max_length=128,
    blank=False,
    null=False,
    verbose_name="Язык"
  )
  small_description = models.CharField(
    max_length=256,
    blank=True,
    null=True,
    verbose_name="Маленькое описание"
  )
  title = models.CharField(
    max_length=128,
    blank=True,
    null=True,
    verbose_name="Заголовок"
  )
  charfields = models.ManyToManyField(
    CharField,
    verbose_name="Средний текст"
  )
  checkfields = models.ManyToManyField(
    CheckField,
    verbose_name="Средний текст"
  )
  textarea = models.TextField(
    blank=True,
    null=True,
    verbose_name="Длинный текст"
  )
  background_image = models.ImageField(
    upload_to=background_image_path,
    blank=True, 
    null=True, 
    verbose_name="Задний фон"
  )
  
  def __str__(self):
    return str(self.title)

  class Meta:
    verbose_name_plural = "Опросы"
    db_table = "polls"
