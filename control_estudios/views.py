from django.shortcuts import render, redirect
from control_estudios.models import *
from control_estudios.forms import *
from django.urls import reverse
from django.db.models import Q
# Create your views here.

def listar_estudiantes(request):
    contexto = {
        
        "Comision":"55350",
        "Escuela":"Codehouse",
        "Autor":"Facu",
        #django urm hace la consulta a la base de datos y retorna la info
        "estudiantes": Estudiante.objects.all()
        #[
        #    {"nombre": "Emanuel", "apellido": "Dautel", "nota": 10},
        #    {"nombre": "Manuela", "apellido": "Gomez", "nota": 4},
        #    {"nombre": "Ivan", "apellido": "Tomasevich", "nota": 6},
        #    {"nombre": "Carlos", "apellido": "Perez", "nota": 1},
        #]
    }
    http_response = render(
        request=request,
        template_name='control_estudios/listar_estudiantes.html',
        context=contexto,
    )
    return http_response


def listar_cursos(request):
    contexto={
        "cursos": Curso.objects.all()
        }
    http_response = render(
        request=request,
        template_name='control_estudios/listar_cursos.html',
        context=contexto,
    )
    return http_response






"""
def crear_curso_version_1(request):
    
    Vista no usada
    Solo con fines academicos de consulta
   
    if request.method == "POST":  # Es un post, user quiere crear curso, hay que cehquear el metodo 
        data = request.POST  # EL request.post almacena un Diccionario con la data del formulario
        nombre = data['nombre']
        comision = data['comision']
        profesor=data['profesor']
        # creo un curso en memoria RAM
        curso = Curso(nombre=nombre, comision=comision, profesor=profesor)
        # .save lo guarda en la base de datos
        curso.save()

        # Envio al usuario a la lista de cursos
        url_exitosa = reverse('Lista de cursos')#el reverse te redirige a una pagina
        return redirect(url_exitosa)
    else:  # GET(solo visualiza)
        http_response = render(
            request=request,
            template_name='control_estudios/crear_cursos.html',
        )
        return http_response
"""

def crear_cursos(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = CursoFormulario(request.POST)#al cosntructor le paso la data del formulario

        if formulario.is_valid():#is.valid es un metodo--> 
            #nos retoruna un booleano true o false, el isvalid lee las validaciones del formulario(maxlenght, maxvalue,)
            #si es falso, se termina el if y va 
            # al httpresponse pasando en contexto 
            # el formulario(que contieene el atributo con los errores, 
            # no es un form vacio, es un form que lleno el usuario) 
            # devuelve los errores de ese formulario, en un atributo que se llama punto errors y retorna falso
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            comision = data["comision"]
            profesor=data["profesor"]
            # creo un curso en memoria RAM
            curso = Curso(nombre=nombre, comision=comision, profesor=profesor)
            # Lo guardan en la Base de datos
            curso.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('Lista de cursos')  # estudios/cursos/
            return redirect(url_exitosa)
        
    
    else:  # GET
        formulario = CursoFormulario()#creo una instancia de formulario vacio

    http_response = render(
        request=request,
        template_name='control_estudios/crear_cursos2.html',
        context={'formulario': formulario}#formulario vacio si es get
    )
    return http_response


def buscar_cursos(request):
   if request.method == "POST":
        data = request.POST#data del fromulario de listar cursos.html
        busqueda = data["busqueda"]#el busqueda entre corchetes viene del html
        # Filtro simple
        cursos = Curso.objects.filter(comision__contains=busqueda)
        # Ejemplo filtro avanzado
        # cursos = Curso.objects.filter(
        #     Q(nombre=busqueda) | Q(comision__contains=busqueda)
        # )
        contexto = {
            "cursos": cursos,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/listar_cursos.html',
            context=contexto,
        )
        return http_response

"""
En resumen, cuando varios valores diferentes están asociados al mismo valor en un diccionario, 
al consultar ese valor, Python te devolverá solo las claves que coinciden con ese valor.
 No te dará información sobre las claves originales que se utilizaron para asignar ese valor.
"""
