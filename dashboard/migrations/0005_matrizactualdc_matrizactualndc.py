# Generated by Django 3.1 on 2020-09-07 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200901_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatrizActualDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo')),
                ('capacidad', models.DecimalField(decimal_places=5, max_digits=7, verbose_name='Capacidad')),
                ('conversion', models.DecimalField(decimal_places=5, max_digits=7, verbose_name='Conversión')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'MatrizActualDC',
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='MatrizActualNDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo')),
                ('capacidad', models.DecimalField(decimal_places=5, max_digits=7, verbose_name='Capacidad')),
                ('conversion', models.DecimalField(decimal_places=5, max_digits=7, verbose_name='Conversión')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'MatrizActualNDC',
                'ordering': ['tipo'],
            },
        ),
    ]
