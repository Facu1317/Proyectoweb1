from django.contrib import admin

# Register your models here.
from control_estudios.models import *

admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Estudiante)
admin.site.register(Profesor)