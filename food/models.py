import imp
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class FoodCategory(models.Model):
    category = models.CharField(max_length=128)
    def __str__(self):
        return self.category

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    calories = models.PositiveIntegerField()
    sodium = models.PositiveIntegerField()
    protien = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    sugars = models.PositiveIntegerField()
    date = models.DateField(default=datetime.date.today, null=True)

