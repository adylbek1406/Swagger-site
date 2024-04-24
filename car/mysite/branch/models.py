from django.db import models
from django.utils import timezone
class Branch(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    address = models.CharField(max_length=255, default=' адреса')
    region = models.CharField(max_length=255, verbose_name='Регион', default='Не указан')
    # data = models.DateField(default=timezone.now().isoformat)
    position = models.CharField(max_length=255, default='Пример позиции')

    def __str__(self):
        return f"{self.name} - {self.address}"