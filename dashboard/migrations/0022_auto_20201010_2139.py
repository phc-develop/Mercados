# Generated by Django 3.0.5 on 2020-10-11 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20201008_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clp',
            name='capacidad',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Capacidad instalada'),
        ),
    ]
