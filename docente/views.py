from django.shortcuts import render, redirect
from processos.models import  Trabajador, Materias, Paralelo, Examen, Tareas, Notas, Cursos, Versiontest



# Create your views here.
def docente_view(request):

    return render(request, 'dbs_docente.html', {})


def versiones_docente_view(request):
    objet_Materias = Materias.objects.filter(estado="A")
    if request.method == "POST":
        materias_id = int(request.POST["asignatura"])
        return redirect('docente:malladc', id=materias_id)
    return render(request, 'versiones.html', {'asignaturas': objet_Materias})


def microcurricular_docente_view(request):

    objasignatura = Materias.objects.filter(estado="A")
    return render(request, 'microcurricular.html', {'asignatura': objasignatura})


def perfildc_view(request):
    datosTrabajador = Trabajador.objects.filter(rol='Profesor')
    msg=""
    return render(request, 'perfil_docente.html', {'datosTrabajador': datosTrabajador, 'msg': msg})


def configuraciondc_view(request):
    return render(request, 'configuraciondc.html', {})


def malladc_view(request, id):
    Materias = Materias.objects.get(id=int(id), estado="A")
    return render(request, 'malladc.html', {
        'Materias': Materias
    })


def vista_pdf(request):
    return render(request, 'index.html', {})

def paralelo_docente(request):
    datosParalelo = Paralelo.objects.filter(estado='A')
    msg=""
    msg1 = ""

    if request.method == 'POST':
        if "eliminar" in request.POST:
            paralelo_id = request.POST["eliminar"]
            try:
                paralelo = Paralelo.objects.get(id=paralelo_id)
                paralelo.estado = "I"
                paralelo.save()
                msg = "Materia eliminada exitosamente."
            except Paralelo.DoesNotExist:
                msg = "El paralelo no existe o ya ha sido eliminada."

        if "crear" in request.POST:
            nombre_cursos = request.POST["nombre_cursos"]

            paralelo = Paralelo(
                nombre_cursos=nombre_cursos,
            )
            paralelo.save()
            msg1 = "Paralelo creado exitosamente."
    return render(request, 'paralelos.html', {'datosParalelo':datosParalelo, 'msg': msg, 'msg1' : msg1})

def examenes_docente(request):
    return render(request, 'examenes.html', {})

def materias_docente_view(request):
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
    return render(request, 'materias.html', {'datosMaterias': datosMaterias, 'msg': msg, 'msg1' : msg1})

def tareas_docente_view(request):
    datosTareas = Tareas.objects.all()
    msg = ""
    msg1 = ""

    if request.method == 'POST':
        if "eliminar" in request.POST:
            tarea_id = request.POST["eliminar"]
            try:
                tarea = Tareas.objects.get(id=tarea_id)
                tarea.delete()
                msg = "Tarea eliminada exitosamente."
            except Tareas.DoesNotExist:
                msg = "La tarea no existe o ya ha sido eliminada."

        if "crear" in request.POST:
            nombre_tarea = request.POST["nombre_tarea"]
            descripcion_tarea = request.POST["descripcion_tarea"]
            paralelo_id = request.POST["paralelo"]

            if nombre_tarea and descripcion_tarea and paralelo_id:
                try:
                    paralelo = Paralelo.objects.get(id=paralelo_id)
                    tarea = Tareas(nombre_tarea=nombre_tarea, descripcion_tarea=descripcion_tarea, paralelo=paralelo)
                    tarea.save()
                    msg1 = "Tarea creada exitosamente."
                except Paralelo.DoesNotExist:
                    msg1 = "El paralelo seleccionado no existe."
            else:
                msg1 = "Todos los campos son requeridos."

    return render(request, 'tareasdc.html', {'datosTareas': datosTareas, 'msg': msg, 'msg1': msg1})


def proyectos_docente_view(request):
    return render(request, 'proyectos.html', {})
