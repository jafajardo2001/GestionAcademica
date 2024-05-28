from django.shortcuts import render, redirect
from processos.models import Asignatura, Trabajador



# Create your views here.
def docente_view(request):

    return render(request, 'dbs_docente.html', {})


def versiones_view(request):
    objet_Asignatura = Asignatura.objects.filter(estado="A")
    if request.method == "POST":
        asignatura_id = int(request.POST["asignatura"])
        return redirect('docente:malladc', id=asignatura_id)
    return render(request, 'versiones.html', {'asignaturas': objet_Asignatura})


def microcurricular_view(request):

    objasignatura = Asignatura.objects.filter(estado="A")
    return render(request, 'microcurricular.html', {'asignatura': objasignatura})


def perfildc_view(request):
    datosTrabajador = Trabajador.objects.filter(rol='Profesor')
    msg=""
    return render(request, 'perfil_docente.html', {'datosTrabajador': datosTrabajador, 'msg': msg})


def configuraciondc_view(request):
    return render(request, 'configuraciondc.html', {})


def malladc_view(request, id):
    asignatura = Asignatura.objects.get(id=int(id), estado="A")
    return render(request, 'malladc.html', {
        'asignatura': asignatura
    })


def vista_pdf(request):
    return render(request, 'index.html', {})

def paralelo(request):
    return render(request, 'paralelos.html', {})

def examenes(request):
    return render(request, 'examenes.html', {})
