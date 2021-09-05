# Generated by Django 3.1.2 on 2021-03-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20210328_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='hito',
            field=models.ManyToManyField(to='portfolio.Hito', verbose_name='Hitos'),
        ),
        migrations.AddField(
            model_name='project',
            name='presupuesto',
            field=models.ManyToManyField(to='portfolio.Budget', verbose_name='Presupuestos'),
        ),
        migrations.AddField(
            model_name='project',
            name='risk',
            field=models.ManyToManyField(to='portfolio.Risk', verbose_name='Riesgos'),
        ),
    ]
