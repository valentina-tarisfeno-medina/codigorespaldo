# Generated by Django 3.1.3 on 2020-12-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('campus_macul', models.CharField(max_length=200)),
                ('campus_providencia', models.CharField(max_length=200)),
                ('casa_central', models.CharField(max_length=6)),
                ('cantidad_estacionamiento', models.CharField(max_length=1000)),
            ],
        ),
    ]