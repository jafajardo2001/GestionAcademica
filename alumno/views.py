from django.shortcuts import render, redirect
from processos.models import Materias, Trabajador


def alumno_view (request):
    return render(request, 'dsb_alumno.html', {})


def perfil_alumno_view (request):
    datosTrabajador = Trabajador.objects.filter(rol='Alumno')
    msg=""
    return render(request, 'perfil_alumno.html', {'datosTrabajador': datosTrabajador, 'msg': msg})

def calificaciones_alumno(request):
    return render(request, 'calificaciones.html', {})

def config_alumno(request):
    return render(request, 'config_al.html', {})

def error(request):
    return render(request, '404.html', {})

def materias_alumno_view(request):
    datosMaterias = Materias.objects.filter(estado='A')
    msg = ""
    msg1 = ""

    if request.method == 'POST':
        if "eliminar" in request.POST:
            materia_id = request.POST["eliminar"]
            try:
                materias = Materias.objects.get(id=materia_id)
                materias.estado = "I"
                materias.save()
                msg = "Materia eliminada exitosamente."
            except Materias.DoesNotExist:
                msg = "La materia no existe o ya ha sido eliminada."

        if "crear" in request.POST:
            nombre_materias = request.POST["nombre_materias"]

            materias = Materias(
                nombre_materias=nombre_materias,
            )
            materias.save()
            msg1 = "Materia creada exitosamente."
    return render(request, 'materias_alu.html', {'datosMaterias': datosMaterias, 'msg': msg, 'msg1' : msg1})

def examenes_alumno(request):
    return render(request, 'examenes.html', {})

def proyectos_alumno(request):
    return render(request, 'proyectos.html')

def tareas_alumno_view(request):
    return render(request, 'tareas.html')


# Create your views here.
