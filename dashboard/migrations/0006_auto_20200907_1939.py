# Generated by Django 3.1 on 2020-09-08 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_matrizactualdc_matrizactualndc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrizactualdc',
            name='conversion',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=7, null=True, verbose_name='Conversión'),
        ),
        migrations.AlterField(
            model_name='matrizactualndc',
            name='conversion',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=7, null=True, verbose_name='Conversión'),
        ),
    ]
