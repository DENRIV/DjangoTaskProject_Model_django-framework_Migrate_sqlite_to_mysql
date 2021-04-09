from django.contrib import admin

# Register your models here.
from . import models 

@admin.register(models.Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion',)
    search_fields = ('nombre',)

@admin.register(models.Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('tarea', 'fecha_creacion',)
    search_fields = ('tarea',)