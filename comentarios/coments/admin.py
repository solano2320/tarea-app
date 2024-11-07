from django.contrib import admin
from django.apps import AppConfig
from .models import Coments

# Register your models here.
admin.site.register(Coments)

# class ComentsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'coments'

