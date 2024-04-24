from django.db import models
from django.contrib.auth.models import User





class Car(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=100)
    invention_date = models.DateField()
    volume = models.DecimalField(max_digits=5, decimal_places=2)

    # models.py

    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        bio = models.TextField(blank=True)
        location = models.CharField(max_length=100, blank=True)
        birth_date = models.DateField(null=True, blank=True)


