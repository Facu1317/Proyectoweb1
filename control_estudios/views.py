from django.shortcuts import render

# Create your views here.

def listar_estudiantes(request):
    contexto = {
        
        "Comision":"55350",
        "Escuela":"Codehouse",
        "Autor":"Facu",

        "estudiantes": [
            {"nombre": "Emanuel", "apellido": "Dautel", "nota": 10},
            {"nombre": "Manuela", "apellido": "Gomez", "nota": 4},
            {"nombre": "Ivan", "apellido": "Tomasevich", "nota": 6},
            {"nombre": "Carlos", "apellido": "Perez", "nota": 1},
        ]
    }
    http_response = render(
        request=request,
        template_name='control_estudios/listar_estudiantes.html',
        context=contexto,
    )
    return http_response


def listar_cursos(request):
    contexto={
        "cursos":[
            {"nombre":"Estadistica II", "profesor":"Vietri"},
            {"nombre":"Analisis Numerico","profesor":"Conocchiari"},
            {"nombre": "Calculo Financiero","profesor":"Millia"},
         ]
        }
    http_response = render(
        request=request,
        template_name='control_estudios/listar_cursos.html',
        context=contexto,
    )
    return http_response