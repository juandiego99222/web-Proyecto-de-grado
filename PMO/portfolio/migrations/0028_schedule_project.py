# Generated by Django 3.1.2 on 2021-08-29 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0027_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.project', verbose_name='Proyecto'),
        ),
    ]