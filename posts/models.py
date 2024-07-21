from django.db import models

# Create your models here.
def image_path(instance, filename):
    return "posts/{category}/{file}".format(category=instance.category.link, file=filename)

class Category(models.Model):
  name = models.CharField(
    max_length=128, 
    blank=False, 
    null=False, 
    verbose_name="Название на английском языке"
  )
  link = models.SlugField(
    max_length=128,
    blank=False,
    null=False,
    verbose_name="Ссылка"
  )
  color = models.CharField(
    max_length=128, 
    blank=False, 
    null=False, 
    verbose_name="Цвет"
  )
  
  def save(self, *args, **kwargs):
    self.name = self.name.lower() # Записать name в нижнем регистре
    super(Category, self).save(*args, **kwargs)
  
  def __str__(self):
    return str(self.name)

  class Meta:
    verbose_name_plural = "Категории"
    db_table = "categories"


class Post(models.Model):
  category = models.ForeignKey(
    Category, 
    blank=False, 
    null=False, 
    on_delete=models.CASCADE,
    verbose_name="Категория"
  )
  TYPE_CHOICES = [
    # В проекте на данный момент имеется лишь два типа карточек для постов
    # Это fact и post
    (1, "post"),
    (2, "fact")
  ]
  type = models.IntegerField(
    choices=TYPE_CHOICES,
    default=None,
    blank=False,
    null=False,
    verbose_name="Type"
  )
  slug = models.SlugField(
    # Используется для создания ссылки на пост
    max_length=128,
    blank=False,
    null=False,
    verbose_name="Slug"
  )
  image = models.ImageField(
    upload_to=image_path,
    blank=True, 
    null=True, 
    verbose_name="Изображение"
  )
  title_ru = models.CharField(
    max_length=256, 
    blank=False, 
    null=False, 
    verbose_name="Заголовок на русском языке"
  )
  title_kz = models.CharField(
    max_length=256, 
    blank=False, 
    null=False, 
    verbose_name="Заголовок на казахском языке"
  )
  description_ru = models.TextField(
    blank=False, 
    null=False, 
    verbose_name="Описание на русском языке"
  )
  description_kz = models.TextField(
    blank=False, 
    null=False, 
    verbose_name="Описание на казахском языке"
  )
  number = models.IntegerField(
    blank=True,
    null=True,
    verbose_name="Номер для факта"
  )
  small_description_ru = models.TextField(
    blank=True,
    null=True,
    verbose_name="Маленькое описание на русском языке"
  )
  small_description_kz = models.TextField(
    blank=True,
    null=True,
    verbose_name="Маленькое описание на казахском языке"
  )
  date = models.DateTimeField(
    null=True,
    blank=True,
    verbose_name="Дата"
  )
  
  def __str__(self):
    return str(self.slug)

  class Meta:
    verbose_name_plural = "Посты"
    db_table = "posts"
  