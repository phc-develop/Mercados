# Generated by Django 3.0.5 on 2020-11-19 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0035_auto_20201119_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clp',
            name='oef_asignada',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True, verbose_name='OEF asignada'),
        ),
    ]
