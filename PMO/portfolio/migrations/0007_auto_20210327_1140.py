# Generated by Django 3.1.2 on 2021-03-27 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_project_interesteds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='interesteds',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.interested', verbose_name='Interesados'),
        ),
    ]
