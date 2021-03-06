# Generated by Django 3.0.5 on 2020-10-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20200928_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adicionales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hidraulica', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Hidraulica')),
                ('liquidos', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Liquidos')),
                ('carbon', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Carbon')),
                ('gas', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Gas')),
                ('glp', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='GLP')),
                ('pch', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='PCH')),
                ('ndc_t', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='NDC_T')),
                ('solar', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Solar')),
                ('eolica', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Eolica')),
                ('expansion_adicional', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Expansión adicional')),
            ],
            options={
                'verbose_name': 'Adicionales',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='CLP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representante_proyecto', models.CharField(max_length=100, verbose_name='Representante del proyecto')),
                ('proyecto', models.CharField(max_length=100, verbose_name='Proyecto')),
                ('clasificacion_planta', models.CharField(max_length=50, verbose_name='Clasificación de la planta')),
                ('oef_asignadas', models.IntegerField(verbose_name='OEF asignadas')),
                ('inicio_vigencia', models.DateField(verbose_name='Inicio vigencia')),
                ('fin_vigencia', models.DateField(verbose_name='Fin vigencia')),
                ('tecnologia', models.CharField(max_length=50, verbose_name='Tecnología')),
                ('capacidad', models.IntegerField(verbose_name='Capacidad instalada')),
                ('fecha_entrada', models.DateField(verbose_name='Fecha entrada')),
            ],
            options={
                'verbose_name': 'CLP',
                'ordering': ['representante_proyecto'],
            },
        ),
        migrations.CreateModel(
            name='ConsolidadoExistente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuente_energia', models.CharField(max_length=100, verbose_name='Fuente de energía')),
                ('planta', models.CharField(blank=True, max_length=100, null=True, verbose_name='planta')),
                ('capacidad', models.IntegerField(blank=True, null=True, verbose_name='Capacidad')),
                ('enficc', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True, verbose_name='ENFICC')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('asignacion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Asignación')),
            ],
            options={
                'verbose_name': 'ConsolidadoExistente',
                'ordering': ['fuente_energia'],
            },
        ),
        migrations.CreateModel(
            name='CrecimientoMW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hidraulica', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Hidraulica')),
                ('liquidos', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Liquidos')),
                ('carbon', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Carbon')),
                ('gas', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Gas')),
                ('glp', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='GLP')),
                ('pch', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='PCH')),
                ('ndc_t', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='NDC_T')),
                ('solar', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Solar')),
                ('eolica', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Eolica')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total')),
            ],
            options={
                'verbose_name': 'CrecimientoMW',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='CxC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representante_proyecto', models.CharField(max_length=100, verbose_name='Representante del proyecto')),
                ('proyecto', models.CharField(max_length=100, verbose_name='Proyecto')),
                ('clasificacion_planta', models.CharField(max_length=50, verbose_name='Clasificación de la planta')),
                ('oef_asignadas', models.IntegerField(verbose_name='OEF asignadas')),
                ('inicio_vigencia', models.DateField(verbose_name='Inicio vigencia')),
                ('fin_vigencia', models.DateField(verbose_name='Fin vigencia')),
                ('tecnologia', models.CharField(max_length=50, verbose_name='Tecnología')),
                ('capacidad', models.IntegerField(verbose_name='Capacidad instalada')),
                ('fecha_entrada', models.DateField(verbose_name='Fecha entrada')),
            ],
            options={
                'verbose_name': 'CxC',
                'ordering': ['representante_proyecto'],
            },
        ),
        migrations.CreateModel(
            name='ExistentesCxCCLP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hidraulica', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Hidraulica')),
                ('liquidos', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Liquidos')),
                ('carbon', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Carbon')),
                ('gas', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Gas')),
                ('glp', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='GLP')),
                ('pch', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='PCH')),
                ('ndc_t', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='NDC_T')),
                ('solar', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Solar')),
                ('eolica', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Eolica')),
                ('existentes_cxc_clp', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Existentes CxC CLP')),
            ],
            options={
                'verbose_name': 'ExistentesCxCCLP',
                'ordering': ['fecha'],
            },
        ),
    ]
