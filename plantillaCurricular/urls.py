from django.contrib import admin
from django.urls import path, include
from processos import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('forgot/', views.forgot_view, name='forgot'),
    path('recover/', views.recover_view, name='recover'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('trabajador/', views.trabajador_view, name='usuarios'),
    path('materias/', views.materias_procesos_view, name='materias'),
    path('paralelos/', views.paralelo_view, name='paralelos'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('tareas/', views.tareas_view, name='tareas'),
    path('examen/', views.examen_view, name='examen'),
    path('notas/', views.notas_view, name='notas'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('configuracion/', views.configuracion_view, name='configuracion'),
    path('admin/', admin.site.urls),
    path('docente/', include('docente.urls'), name="docente"),
    path('alumno/', include('alumno.urls'), name="alumno")
]
