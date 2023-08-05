# Generated by Django 4.2.3 on 2023-07-31 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('processos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_asignatura', models.CharField(max_length=200)),
                ('objetivo_asignatura', models.CharField(max_length=650)),
                ('aportes_teoricos', models.CharField(max_length=1500)),
                ('objetivos_especificos', models.CharField(max_length=1500)),
                ('producto_academico', models.CharField(max_length=1500)),
                ('prerequisito_academico', models.CharField(max_length=400)),
                ('periodo', models.CharField(max_length=150)),
                ('estado', models.CharField(default='A', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Referencias',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_referencia', models.CharField(max_length=100)),
                ('numero_referencia', models.IntegerField()),
                ('titulo_obra', models.CharField(max_length=500)),
                ('existencia_biblioteca', models.CharField(max_length=450)),
                ('numero_ejemplares', models.IntegerField()),
                ('estado', models.CharField(default='A', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('cedula_identidad', models.IntegerField(unique=True)),
                ('correo', models.EmailField(max_length=300)),
                ('contrasena', models.CharField(max_length=150)),
                ('rol', models.CharField(max_length=60)),
                ('estado', models.CharField(default='A', max_length=3)),
            ],
        ),
    ]
