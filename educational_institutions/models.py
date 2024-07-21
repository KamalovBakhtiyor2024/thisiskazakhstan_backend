from django.db import models

# Create your models here.
class EducationalInstitution(models.Model):
  name_ru = models.CharField(
    max_length=128, 
    blank=False, 
    null=False,
    verbose_name="Название на русском языке"
  )
  name_kz = models.CharField(
    max_length=128, 
    blank=False, 
    null=False,
    verbose_name="Название на казахском языке"
  )
  TYPE_CHOICES = [
    (1, "school"),
    (2, "college"),
    (3, "university")
  ]
  type = models.IntegerField(
    choices=TYPE_CHOICES,
    default=None,
    blank=False,
    null=False,
    verbose_name="Тип образовательного учреждения"
  )
  address = models.CharField(
    max_length=125,
    blank=False,
    null=False,
    verbose_name="Адрес"
  )
  work_time = models.CharField(
    max_length=125,
    blank=False,
    null=False,
    verbose_name="Рабочее время"
  )

  def __str__(self):
    return str(self.name_ru)

  class Meta:
    verbose_name_plural = "Образовательные учреждения"
    db_table = "educational_institutions"
