# Generated by Django 3.0.9 on 2022-04-28 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='distance',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='reps',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='sets',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
