from django.contrib import admin
from .models import Poll, CharField, CheckField

# Register your models here.
admin.site.register(Poll)
admin.site.register(CharField)
admin.site.register(CheckField)
