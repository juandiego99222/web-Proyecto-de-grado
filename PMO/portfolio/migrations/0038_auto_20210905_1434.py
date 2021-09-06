# Generated by Django 3.1.2 on 2021-09-05 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0037_auto_20210905_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='duration',
        ),
        migrations.AddField(
            model_name='schedule',
            name='estado',
            field=models.CharField(blank=True, choices=[('En Progreso', 'En Progreso'), ('Terminada', 'Terminada')], max_length=32, null=True),
        ),
    ]
