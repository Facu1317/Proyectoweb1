from django.db import models
from django.core import validators

# Create your models here.

class Curso(models.Model):
    #Los atributos de clase son las columnas en la bd
    nombre=models.CharField(max_length=64, validators=[validators.RegexValidator(r'^[A-Za-z ]*$', 'Ingrese un nombre sin numeros.')])
    comision=models.IntegerField()
    profesor=models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.comision}, {self.profesor}"
    


class Estudiante(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    dni=models.CharField(max_length=32)
    email=models.EmailField(blank=True)
    nota=models.IntegerField(blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}"
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    dni=models.CharField(max_length=32)
    email=models.EmailField(blank=True)
    biografia=models.TextField(blank=True)
    dedicacion=models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}, {self.dedicacion}"

class Entregable(models.Model):
    nombre=models.CharField(max_length=256)
    fecha_entrega=models.DateTimeField(auto_now_add=True)
    esta_aprobado=models.BooleanField(default=False)




