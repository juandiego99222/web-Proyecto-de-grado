# Generated by Django 3.1.2 on 2021-03-27 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20210327_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='interesteds',
        ),
    ]
