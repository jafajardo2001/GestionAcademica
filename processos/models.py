from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Trabajador(models.Model):
    id = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    cedula_identidad = models.IntegerField(unique=True)
    correo = models.EmailField(max_length=300)
    contrasena = models.CharField(max_length=150)
    rol = models.CharField(max_length=60)
    estado = models.CharField(max_length=3, default='A')

class Alumno(models.Model):
    id = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    cedula_identidad = models.IntegerField(unique=True)
    correo = models.EmailField(max_length=300)
    contrasena = models.CharField(max_length=150)
    rol = models.CharField(max_length=60)
    estado = models.CharField(max_length=3, default='A')
    
class Materias(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_materias = models.CharField(max_length=200)
    estado = models.CharField(max_length=3, default='A')

class Paralelo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_cursos = models.CharField(max_length=50)
    estado = models.CharField(max_length=3, default='A')
    
class Notas(models.Model):
    id = models.IntegerField(primary_key=True)
    nombres_notas = models.CharField(max_length=150)
    estado = models.CharField(max_length=3, default='A')
    
class Tareas(models.Model):
    id = models.IntegerField(primary_key=True)
    calificaciones = models.BooleanField()
    estado = models.CharField(max_length=3, default='A')
    
class Examen(models.Model):
    id = models.IntegerField(primary_key=True)
    califaciones = models.BooleanField()
    estado = models.CharField(max_length=3, default='A')

class Cursos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_curso = models.CharField(max_length=50)
    estado = models.CharField(max_length=3, default='A')

class Versiontest(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_version = models.CharField(max_length=200)
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=3, default='A')
