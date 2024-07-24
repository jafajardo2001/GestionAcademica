# Generated by Django 5.0.7 on 2024-07-24 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0010_cursos_examen_materias_notas_paralelo_tareas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('editorial', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateField()),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('participantes', models.ManyToManyField(related_name='actividades', to='processos.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_matricula', models.DateTimeField(auto_now_add=True)),
                ('activa', models.BooleanField(default=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.cursos')),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.TextField()),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
                ('leido', models.BooleanField(default=False)),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_recibidos', to='processos.trabajador')),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_enviados', to='processos.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=500)),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='processos.encuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(auto_now_add=True)),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('devuelto', models.BooleanField(default=False)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.alumno')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.libro')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaEncuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('respuesta', models.TextField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.alumno')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='processos.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.trabajador')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='processos.tema')),
            ],
        ),
        migrations.CreateModel(
            name='TicketSoporte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asunto', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('resuelto', models.BooleanField(default=False)),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.trabajador')),
            ],
        ),
    ]