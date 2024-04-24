
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



from rest_framework.generics import ListCreateAPIView
from .models import Car
from .serializers import CarSerializer

class CarListCreateView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    template_name = 'rest_framework/api.html'  # Укажите правильный путь к шаблону




# ваше_название_приложения/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Car
from .serializers import CarSerializer

class CarListCreateView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
