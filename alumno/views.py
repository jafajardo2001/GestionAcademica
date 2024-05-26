from django.shortcuts import render

def alumno_view (request):
    return render(request, 'dsb_alumno.html', {})

def perfil_view (request):
    return render(request, 'perfil_alumno.html', {})

def calificaciones(request):
    return render(request, 'calificaciones.html', {})

def config_alumno(request):
    return render(request, 'config_al.html', {})

def error(request):
    return render(request, '404.html', {})

def materias(request):
    return render(request, 'materias.html', {})

def examenes(request):
    return render(request, 'examenes.html', {})

def proyectos(request):
    return render(request, 'proyectos.html')

# Create your views here.
