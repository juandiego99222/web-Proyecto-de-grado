# Generated by Django 3.1.2 on 2021-05-11 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_auto_20210509_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='amountBudget',
            field=models.IntegerField(verbose_name='Cantidad en Pesos'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='descriptionBudget',
            field=models.CharField(max_length=200, verbose_name='Descripción Presupuesto'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='amountCost',
            field=models.IntegerField(verbose_name='Cantidad en Pesos'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='descriptionCost',
            field=models.CharField(max_length=200, verbose_name='Descripción Costo'),
        ),
        migrations.AlterField(
            model_name='hito',
            name='descriptionHito',
            field=models.CharField(max_length=400, verbose_name='Descripción Hito'),
        ),
        migrations.AlterField(
            model_name='interested',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre Interesado'),
        ),
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Nombre Proyecto'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='descriptionRisk',
            field=models.CharField(max_length=400, verbose_name='Descripción Riesgo'),
        ),
    ]