from django.contrib import admin
from django.urls import path
from docente import views


app_name = "docente"
urlpatterns = [
    path('', views.docente_view, name='docente'),
    path('horario/', views.versiones_view, name='horario'),
    path('paralelo/', views.paralelo, name='paralelo'),
    path('examenes/', views.examenes, name='examenes'),
    path('calificaciones/', views.microcurricular_view, name="calificaciones"),
    path('perfil/', views.perfildc_view, name='perfil'),
    path('configuracion/', views.configuraciondc_view, name='configuracion'),
    path('malla/<int:id>', views.malladc_view, name='malladc'),
    path('pdf/', views.vista_pdf, name='pdf'),
]
