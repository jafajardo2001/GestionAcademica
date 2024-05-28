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


class Asignatura(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_asignatura = models.CharField(max_length=200)
    objetivo_asignatura = models.CharField(max_length=650)
    aportes_teoricos = models.CharField(max_length=1500)
    objetivos_especificos = models.CharField(max_length=1500)
    producto_academico = models.CharField(max_length=1500)
    prerequisito_academico = models.CharField(max_length=400)
    periodo = models.CharField(max_length=150)
    aportes_perfil_egreso = models.CharField(max_length=600)
    estado = models.CharField(max_length=3, default='A')


class Referencias(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_referencia = models.CharField(max_length=100)
    numero_referencia = models.IntegerField()
    titulo_obra = models.CharField(max_length=500)
    existencia_biblioteca = models.CharField(max_length=450)
    numero_ejemplares = models.IntegerField()
    estado = models.CharField(max_length=3, default='A')


class ProductoAcademico(models.Model):
    id = models.IntegerField(primary_key=True)
    producto_final = models.CharField(max_length=500)
    objetivo = models.TextField()
    producto_parcial = models.TextField()
    presentacion = models.TextField()
    integracion = models.TextField()
    estado = models.CharField(max_length=3, default='A')


class Unidades(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_unidad = models.CharField(max_length=200)
    objetivo_unidad = models.CharField(max_length=650)
    numero_unidad = models.IntegerField()
    horas_docencia = models.IntegerField()
    horas_practica = models.IntegerField()
    estado = models.CharField(max_length=3, default='A')


class Contenido(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_contenido = models.CharField(max_length=200)
    numero_contenido = models.IntegerField()
    estado = models.CharField(max_length=3, default='A')


class Versiontest(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_version = models.CharField(max_length=200)
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=3, default='A')


class Responsables(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_responsable = models.CharField(max_length=200)
    cargo_responsable = models.CharField(max_length=200)
    firma_responsable = models.CharField(max_length=200)
    estado = models.CharField(max_length=3, default='A')


class Controlador(models.Model):
    id = models.IntegerField(primary_key=True)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    # Sin el apóstrofo al final de 'CASCADE'
    referencia = models.ForeignKey(Referencias, on_delete=models.CASCADE)
    producto_academico = models.ForeignKey(
        ProductoAcademico, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidades, on_delete=models.CASCADE)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsables, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3, default='A')
