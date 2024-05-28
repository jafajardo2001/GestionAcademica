from django.contrib import admin
from django.urls import path, include
from processos import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('forgot/', views.forgot_view, name='forgot'),
    path('recover/', views.recover_view, name='recover'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('datosinformativos/', views.datosinfo_view, name='datosinfo'),
    path('datosguardados', views.datosrg_view, name='datosguardados'),
    path('trabajador', views.trabajador_view, name='usuarios'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('configuracion/', views.configuracion_view, name='configuracion'),
    path('controlador/', views.controlador_view, name='controlador'),
    path('mallaCurricular/<int:id>',
         views.mallaCurricular_view, name='mallaCurricular'),
    path('admin/', admin.site.urls),
    path('docente/', include('docente.urls'), name="docente"),
    path('alumno/', include('alumno.urls'), name="alumno")
]
