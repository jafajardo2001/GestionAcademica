from django.contrib import admin
from django.urls import path
from alumno import views


app_name = "alumno"
urlpatterns = [
    path('', views.alumno_view, name='alumno'),
    path('examenes/', views.examenes_alumno, name='examenes'),
    path('calificaciones/', views.calificaciones_alumno, name="planificacion"),
    path('perfil/', views.perfil_alumno_view, name='perfil'),
    path('configuracion/', views.config_alumno, name='configuracion'),
    path('proyectos>', views.proyectos_alumno, name='proyectos'),
    path('error/', views.error, name='pdf'),
    path('materias/', views.materias_alumno_view, name='materiasalu'),
    path('tareas/', views.tareas_alumno_view, name='tareas'),
]
