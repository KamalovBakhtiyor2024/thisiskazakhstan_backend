from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
  category = CategorySerializer()
  date = serializers.DateTimeField(format="%Y-%m-%d")
  
  class Meta:
    model = Post
    fields = [
      "category",
      "description_ru",
      "description_kz",
      "small_description_ru",
      "small_description_kz",
      "type",
      "title_ru",
      "title_kz",
      "number",
      "image",
      "slug",
      "date"
    ]
