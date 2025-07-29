from django.urls import path
from .views import lista_trabajadores

urlpatterns = [
    path('lista/', lista_trabajadores, name='lista'),
]