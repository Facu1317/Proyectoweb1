from django.contrib import admin
from django.urls import path
from control_estudios.views import listar_estudiantes

#Urls especificas de la app
urlpatterns = [
    
    path("listarEstudiantes/", listar_estudiantes)
]
