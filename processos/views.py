from django.shortcuts import redirect, render, HttpResponse
from .models import Trabajador, Materias, Notas, Cursos, Paralelo, Tareas, Examen, Versiontest
from django.db import transaction
from django.contrib.auth.decorators import login_required


def login_view(request):
    ok = None
    msg = None
    if request.method == "POST":
        usuarioInput = request.POST["username"]
        claveInput = request.POST["password"]
        try:
            objtrabajado = Trabajador.objects.get(correo=usuarioInput)
            print(objtrabajado)
            if objtrabajado:
                if (objtrabajado and objtrabajado.contrasena == claveInput):
                    if objtrabajado.rol == "Admin":
                        return redirect('dashboard')
                    elif objtrabajado.rol == "Profesor":
                        return redirect('docente:docente')
                    elif objtrabajado.rol == "Alumno":
                        return redirect('alumno:alumno')
                else:
                    msg = "Credenciales invalidas"
                    ok = False
                    print("error credenciales")
        except:
            print("error ren la base de datos")
            ok = False
            msg = "Este usuario no está registrado en nuestra base de datos"

    return render(request, 'login.html', {
        'ok': ok,
        'msg': msg
    })


def dashboard_view(request):

    return render(request, 'dashboard.html', {})


def forgot_view(request):
    return render(request, 'forgot.html', {})


def recover_view(request):
    return render(request, 'recoverpsw.html', {})

def trabajador_view(request):
    datosTrabajador = Trabajador.objects.filter(estado='A')
    msg = ""
    msg1 = ""

    if request.method == 'POST':
        if "eliminar" in request.POST:
            trabajador_id = request.POST["eliminar"]
            try:
                trabajador = Trabajador.objects.get(id=trabajador_id)
                trabajador.estado = "I"
                trabajador.save()
                msg = "Trabajador eliminado exitosamente."
            except Trabajador.DoesNotExist:
                msg = "El trabajador no existe o ya ha sido eliminado."

        if "crear" in request.POST:
            nombres_trab = request.POST["nombres_trab"]
            apellidos_trab = request.POST["apellidos_trab"]
            cedula_trab = request.POST["cedula_trab"]
            correo_trab = request.POST["correo_trab"]
            contrasena_trab = request.POST["contrasena_trab"]
            rol_trab = request.POST["rol_trab"]

            trabajador = Trabajador(
                nombres=nombres_trab,
                apellidos=apellidos_trab,
                cedula_identidad=cedula_trab,
                correo=correo_trab,
                contrasena=contrasena_trab,
                rol=rol_trab
            )
            trabajador.save()
            msg1 = "Trabajador creado exitosamente."
    return render(request, 'Registrar.html', {'datosTrabajador': datosTrabajador, 'msg': msg, 'msg1': msg1})

def materias_view(request):
    datosMaterias = Materias.objects.filter(estado='A')
    msg=""
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

def notas_view(request):
    datosNotas = Notas.objects.filter(estado='A')
    msg=""
    return render(request, 'notas.html', {'datosNotas': datosNotas, 'msg':msg})

def paralelo_view(request):
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
    return render(request, 'paralelos.html', {'datosParalelo': datosParalelo, 'msg': msg, 'msg1' : msg1})

def cursos_view(request):
    datosCursos = Cursos.objects.filter(estado='A')
    msg=""
    return render(request, 'cursos,html', {'datosCursos': datosCursos, 'msg': msg})

def tareas_view(request):
    datosTareas =Tareas.objects.filter(estado='A')
    msg=""
    return render(request, 'tareas.html', {'datosTareas': datosTareas, 'msg': msg})

def examen_view(request):
    datosExamen = Examen.objects.filter(estado='A')
    msg=""
    return render(request, 'examen.html', {'datosExamen': datosExamen, 'msg': msg})

def perfil_view(request):
    datosTrabajador = Trabajador.objects.filter(rol='Admin')
    msg=""
    return render(request, 'perfil.html', {'datosTrabajador': datosTrabajador, 'msg': msg})

def configuracion_view(request):
    return render(request, 'configuracion.html', {})
