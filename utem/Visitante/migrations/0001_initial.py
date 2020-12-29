# Generated by Django 3.1.3 on 2020-12-28 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
                ('Rut', models.CharField(max_length=200)),
                ('Patente', models.CharField(max_length=30)),
                ('Sede', models.CharField(choices=[('Casa central', 'Casa central'), ('Campus macul', 'Campus macul'), ('Campus providencia', 'Campus providencia')], default='Casa central', max_length=100)),
                ('Fecha_Ingreso', models.DateTimeField(auto_now_add=True)),
                ('Fecha_Salida', models.DateField()),
                ('Motivo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Visitantemacul',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
                ('Rut', models.CharField(max_length=200)),
                ('Patente', models.CharField(max_length=30)),
                ('Sede', models.CharField(choices=[('Casa central', 'Casa central'), ('Campus macul', 'Campus macul'), ('Campus providencia', 'Campus providencia')], default='Campus macul', max_length=100)),
                ('Fecha_Ingreso', models.DateTimeField(auto_now_add=True)),
                ('Fecha_Salida', models.DateField()),
                ('Motivo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Visitanteprovidencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
                ('Rut', models.CharField(max_length=200)),
                ('Patente', models.CharField(max_length=30)),
                ('Sede', models.CharField(choices=[('Casa central', 'Casa central'), ('Campus macul', 'Campus macul'), ('Campus providencia', 'Campus providencia')], default='Campus providencia', max_length=100)),
                ('Fecha_Ingreso', models.DateTimeField(auto_now_add=True)),
                ('Fecha_Salida', models.DateField()),
                ('Motivo', models.CharField(max_length=1000)),
            ],
        ),
    ]
