from django.urls import path
from .views import empleados


urlpatterns = [
    path('lista/', empleados, name='lista'),
]