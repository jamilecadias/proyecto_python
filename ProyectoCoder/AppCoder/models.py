from django.db import models

# Create your models here.


class Alumnos(models.Model):
    nombreCompleto = models.CharField(max_length=40)
    telefono = models.IntegerField()
    fechaNac = models.DateField()
    curso = models.CharField(max_length=20)


class Clases(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    horario = models.DateTimeField(max_length=60)
    dias = models.CharField(max_length=40)
    
    
class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    sobre = models.CharField(max_length=500)
    cursos = models.CharField(max_length=60)
    foto = models.ImageField()


