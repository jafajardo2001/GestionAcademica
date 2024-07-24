from django.contrib import admin
from django.urls import path
from alumno import views


app_name = "alumno"
urlpatterns = [
    path('', views.alumno_view, name='alumno'),
    path('examenes/', views.examenes, name='examenes'),
    path('calificaciones/', views.calificaciones, name="planificacion"),
    path('perfil/', views.perfil_view, name='perfil'),
    path('configuracion/', views.config_alumno, name='configuracion'),
    path('proyectos>', views.proyectos, name='proyectos academicos'),
    path('error/', views.error, name='pdf'),
    path('materias/', views.materias_view, name='materias'),
]
