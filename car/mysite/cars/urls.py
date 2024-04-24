# ваше_название_приложения/urls.py
from django.urls import path
from .views import CarListCreateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import CarListCreateView, CarRetrieveUpdateDestroyView
from django.contrib import admin



schema_view = get_schema_view(
    openapi.Info(
        title="Car API",
        default_version='v1',
        description="API for managing cars",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyView.as_view(), name='car-detail'),
    path('admin/', admin.site.urls),
]
