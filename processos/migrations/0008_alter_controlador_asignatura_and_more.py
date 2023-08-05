# Generated by Django 4.2.4 on 2023-08-05 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0007_alter_controlador_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlador',
            name='asignatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.asignatura'),
        ),
        migrations.AlterField(
            model_name='controlador',
            name='contenido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.contenido'),
        ),
        migrations.AlterField(
            model_name='controlador',
            name='producto_academico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.productoacademico'),
        ),
        migrations.AlterField(
            model_name='controlador',
            name='referencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.referencias'),
        ),
        migrations.AlterField(
            model_name='controlador',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.responsables'),
        ),
        migrations.AlterField(
            model_name='controlador',
            name='unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processos.unidades'),
        ),
    ]