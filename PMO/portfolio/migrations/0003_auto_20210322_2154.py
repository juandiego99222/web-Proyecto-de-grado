# Generated by Django 3.1.2 on 2021-03-23 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210322_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='completed',
            field=models.DateTimeField(verbose_name='Fecha de finalizacion'),
        ),
    ]
