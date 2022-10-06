# Generated by Django 4.0.6 on 2022-08-19 06:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=100)),
                ('time', models.DateTimeField(verbose_name=datetime.datetime.now)),
            ],
        ),
    ]