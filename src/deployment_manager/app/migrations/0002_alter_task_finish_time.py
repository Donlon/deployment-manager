# Generated by Django 4.0.4 on 2022-04-17 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finish_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
