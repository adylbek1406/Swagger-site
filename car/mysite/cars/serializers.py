# ваше_название_приложения/serializers.py
from rest_framework import serializers
from .models import Car
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

