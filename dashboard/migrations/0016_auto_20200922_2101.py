# Generated by Django 3.1 on 2020-09-23 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20200922_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantas',
            name='enficc_no_comprometida',
            field=models.IntegerField(blank=True, null=True, verbose_name='ENFICC no comprometida'),
        ),
        migrations.AlterField(
            model_name='plantas',
            name='enficc_verificada',
            field=models.IntegerField(blank=True, null=True, verbose_name='ENFICC verificada'),
        ),
    ]
