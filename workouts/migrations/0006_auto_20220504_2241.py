# Generated by Django 3.0.9 on 2022-05-04 22:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_auto_20220504_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
