from django.shortcuts import redirect, render, HttpResponse
from .models import Trabajador, Asignatura, Referencias, ProductoAcademico, Unidades, Controlador
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


def datosinfo_view(request):
    datosAsignatura = Asignatura.objects.filter(estado='A')
    msg = ""
    msg1 = ""

    if request.method == 'POST':
        if "eliminar" in request.POST:
            asignatura_id = request.POST["eliminar"]
            try:
                asignatura = Asignatura.objects.get(id=asignatura_id)
                asignatura.estado = "I"
                asignatura.save()
                msg = "Trabajador eliminado exitosamente."
            except Asignatura.DoesNotExist:
                msg = "Registro eliminado exitosamente."

        if "crear" in request.POST:
            asignatura = request.POST["nombre_asig"]
            periodo_a = request.POST["periodo_asig"]
            prerequisitos = request.POST["prerequisitos_acade"]
            aportes = request.POST["aportes_teori"]
            objetivo = request.POST["objetivo_asig"]
            objetivos_es = request.POST["objetivos_especi"]
            aportes_egreso = request.POST["aportes_perfil"]
            producto_ac = request.POST["producto_academ"]

            asignatura = Asignatura(
                nombre_asignatura=asignatura,
                objetivo_asignatura=objetivo,
                aportes_teoricos=aportes,
                objetivos_especificos=objetivos_es,
                producto_academico=producto_ac,
                prerequisito_academico=prerequisitos,
                periodo=periodo_a,
                aportes_perfil_egreso=aportes_egreso
            )
            asignatura.save()
            msg1 = "Registro exitoso."
    return render(request, 'datosinfo.html', {'datosAsignatura':
                                              datosAsignatura, 'msg': msg,  'msg1': msg1})


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


def producto_view(request):
    datosProducto = ProductoAcademico.objects.filter(estado='A')
    msg = ''

    if request.method == 'POST' and "crear" in request.POST:
        producto_f = request.POST["producto_final"]
        objetivo_p = request.POST["objetivo"]
        producto_p = request.POST["producto_parci"]
        resultados_p = request.POST["resultados_presen"]
        integracion_as = request.POST["integracion_asigna"]

        producto = ProductoAcademico(
            producto_final=producto_f,
            objetivo=objetivo_p,
            producto_parcial=producto_p,
            presentacion=resultados_p,
            integracion=integracion_as
        )
        producto.save()
    return render(request, 'datosinfo.html', {'datosProducto': datosProducto, 'msg': msg})


def referencias_view(request):
    datosReferencias = Referencias.objects.filter(estado='A')
    msg = ""

    if request.method == 'POST' and "crear" in request.POST:
        referencia = request.POST["tipo_referen"]
        numero_ref = request.POST["numero_referen"]
        titulo = request.POST["titulo_obra"]
        biblioteca = request.POST["existencia_biblioteca"]
        numero = request.POST["numero_ejemplar"]

        referencias = Referencias(
            tipo_referencia=referencia,
            numero_referencia=numero_ref,
            titulo_obra=titulo,
            existencia_biblioteca=biblioteca,
            numero_ejemplares=numero
        )
        referencias.save()
    return render(request, 'datosinfo.html', {'datosReferencias':
                                              datosReferencias, 'msg': msg})


def unidades_view(request):
    datosUnidades = Unidades.objects.filter(estado='A')
    msg = ""
    msg1 = ""

    if request.method == 'POST':
        if "eliminar" in request.POST:
            unidades_id = request.POST["eliminar"]
            try:
                unidades = Unidades.objects.get(id=unidades_id)
                unidades.estado = "I"
                unidades.save()
                msg = "Unidad eliminada exitosamente."
            except Unidades.DoesNotExist:
                msg = "Registro eliminado exitosamente."

        if "crear" in request.POST:
            unidad = request.POST["nombre_uni"]
            objetivo_u = request.POST["objetivo_uni"]
            numero_u = request.POST[""]
            horas_do = request.POST["horas_doce"]
            horas_pra = request.POST["horas_pract"]

            unidades = Asignatura(
                nombre_unidad=unidad,
                objetivo_unidad=objetivo_u,
                numero_unidad=numero_u,
                horas_docencia=horas_do,
                horas_practica=horas_pra,
            )
            unidades.save()
            msg1 = "Registro exitoso."
    return render(request, 'datosinfo.html', {'datosUnidades':
                                              datosUnidades, 'msg': msg})


def datosrg_view(request):
    return render(request, 'datosrg.html', {})


def perfil_view(request):
    datosTrabajador = Trabajador.objects.filter(rol='Admin')
    msg=""
    return render(request, 'perfil.html', {'datosTrabajador': datosTrabajador, 'msg': msg})


def configuracion_view(request):
    return render(request, 'configuracion.html', {})


def controlador_view(request):
    objet_Asignatura = Asignatura.objects.filter(estado="A")
    if request.method == "POST":
        asignatura_id = int(request.POST["asignatura"])
        return redirect('mallaCurricular', id=asignatura_id)
    return render(request, 'controlador.html', {'asignaturas': objet_Asignatura})


def mallaCurricular_view(request, id):
    try:
        asignatura = Asignatura.objects.filter(id=int(id), estado='A')
        logger.warning('Esta es una alerta importante')
        # controladores = Controlador.objects.filter(pk=asignatura)
    except:
        return redirect('controlador')

    return render(request, 'malla.html', {
        'asignatura': asignatura
    })
