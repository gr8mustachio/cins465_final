import imp
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class MuscleGroup(models.Model):
    group = models.CharField(max_length=128)
    def __str__(self):
        return self.group

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    musclegroup = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField(null=True)
    reps = models.PositiveIntegerField(null=True)
    distance = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    duration = models.DurationField()
    calsburned = models.PositiveIntegerField()
    heartAvg = models.PositiveSmallIntegerField()
    date = models.DateField(default=datetime.date.today, null=True)