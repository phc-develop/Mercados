# Generated by Django 3.0.5 on 2020-10-08 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20201008_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demanda',
            name='dia_mes',
            field=models.IntegerField(verbose_name='Día mes'),
        ),
    ]
