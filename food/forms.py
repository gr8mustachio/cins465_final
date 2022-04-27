from unicodedata import category
from django import forms 
from food.models import FoodItem, FoodCategory

class FoodForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size' : '80'}))
    category = forms.ModelChoiceField(queryset=FoodCategory.objects.all())
    calories = forms.IntegerField()
    sodium = forms.IntegerField()
    protien = forms.IntegerField()
    carbs = forms.IntegerField()
    fats = forms.IntegerField()
    sugars = forms.IntegerField()