# Generated by Django 3.1.2 on 2021-03-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20210328_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Phase',
            new_name='phase',
        ),
        migrations.AddField(
            model_name='project',
            name='cost',
            field=models.ManyToManyField(to='portfolio.Cost', verbose_name='costos'),
        ),
    ]
