from django.shortcuts import render, redirect
from processos.models import  Trabajador, Materias



# Create your views here.
def docente_view(request):

    return render(request, 'dbs_docente.html', {})


def versiones_view(request):
    objet_Materias = Materias.objects.filter(estado="A")
    if request.method == "POST":
        materias_id = int(request.POST["asignatura"])
        return redirect('docente:malladc', id=materias_id)
    return render(request, 'versiones.html', {'asignaturas': objet_Materias})


def microcurricular_view(request):

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

def paralelo(request):
    return render(request, 'paralelos.html', {})

def examenes(request):
    return render(request, 'examenes.html', {})
