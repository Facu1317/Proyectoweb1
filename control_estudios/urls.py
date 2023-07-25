from django.contrib import admin
from django.urls import path
from control_estudios.views import *

#Urls especificas de la app
urlpatterns = [
    
    path("listarEstudiantes/", listar_estudiantes),
    path("listarCursos/", listar_cursos)
]
