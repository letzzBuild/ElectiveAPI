# Generated by Django 3.2 on 2021-06-15 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='dob',
            field=models.DateField(default=datetime.date(2021, 6, 15)),
        ),
    ]
