# Generated by Django 3.1.2 on 2021-03-23 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='completed',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de finalizacion'),
        ),
    ]