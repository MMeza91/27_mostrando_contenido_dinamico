from django.shortcuts import render
from .models import Listado

# Create your views here.
def lista_trabajadores(request):
    viejos = Listado.objects.all()
    return render(request, 'trabajadores.html', {'listado_viejos' : viejos })