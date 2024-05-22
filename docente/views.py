from django.shortcuts import render, redirect
from processos.models import Asignatura


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
    return render(request, 'perfil_docente.html', {})


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
