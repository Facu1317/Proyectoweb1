from django.db import models

# Create your models here.

class Curso(models.Model):
    #Los atributos de clase son las columnas en la bd
    nombre=models.CharField(max_length=64)
    comision=models.IntegerField()
    


class Estudiante(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    dni=models.CharField(max_length=32)
    email=models.EmailField(blank=True)
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    dni=models.CharField(max_length=32)
    email=models.EmailField(blank=True)
    biografia=models.TextField(blank=True)
    dedicacion=models.CharField(max_length=128)

class Entregable(models.Model):
    nombre=models.CharField(max_length=256)
    fecha_entrega=models.DateTimeField(auto_now_add=True)
    esta_aprobado=models.BooleanField(default=False)




