# Generated by Django 3.1.2 on 2021-09-06 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0039_auto_20210905_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='interested',
            name='influencia',
            field=models.CharField(blank=True, choices=[('Baja', 'Baja'), ('Alta', 'Alta')], max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='interested',
            name='interes',
            field=models.CharField(blank=True, choices=[('Bajo', 'Bajo'), ('Alto', 'Alto')], max_length=32, null=True),
        ),
    ]
