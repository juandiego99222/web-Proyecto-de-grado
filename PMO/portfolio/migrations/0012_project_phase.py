# Generated by Django 3.1.2 on 2021-03-28 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20210328_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Phase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.phase', verbose_name='Fase'),
        ),
    ]
