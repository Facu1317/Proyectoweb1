#   VIEWS SERIAN LOS CONTROLADORES, LAS FUNCIONES
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludar(request):
    saludo="Hola la concha de tu madre por fin puedo tener una interfaz grafica forro"
    respuesta_http=HttpResponse(saludo) 
    return respuesta_http

def saludar_con_fecha(request):
    Fecha_hoy=datetime.now()
    saludo_con_fecha=f"Hola forro, hoy es {Fecha_hoy.day}/{Fecha_hoy.month}"
    respuesta_http=HttpResponse(saludo_con_fecha)
    return respuesta_http

def inicio(request):
    contexto={
        "Autor":"Facu",
        "Escuela":"Codehouse",
        "Comision":"55350",
    }
    
    http_response= render(
        request=request,
        template_name="inicio.html",
        context=contexto,
        )
    return http_response


