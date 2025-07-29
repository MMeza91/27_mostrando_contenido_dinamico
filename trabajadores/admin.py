from django.contrib import admin
from .models import Listado

# Register your models here.
@admin.register(Listado)
class ListadoAdmin(admin.ModelAdmin):
    pass
