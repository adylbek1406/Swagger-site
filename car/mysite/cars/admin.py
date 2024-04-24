# ваше_название_приложения/admin.py
from django.contrib import admin
from .models import Car

admin.site.register(Car)
