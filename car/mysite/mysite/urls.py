# mysite/urls.py
from django.urls import path, include

urlpatterns = [

    path('api/', include('cars.urls')),
    path('api/', include('branch.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
