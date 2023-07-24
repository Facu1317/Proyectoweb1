from django.contrib import admin
from django.urls import path
from control_estudios.views import listar_estudiantes, listar_cursos

#Urls especificas de la app
urlpatterns = [
    
    path("listarEstudiantes/", listar_estudiantes),
    path("listarCursos/", listar_cursos)
]
