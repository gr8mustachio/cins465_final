from unicodedata import category
from django import forms 
from food.models import Food, FoodCategory

class FoodForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size' : '80'}))
    date = forms.DateField()
    category = forms.ModelChoiceField(queryset=FoodCategory.objects.all())
    calories = forms.IntegerField()
    sodium = forms.IntegerField()
    protien = forms.IntegerField()
    carbs = forms.IntegerField()
    fats = forms.IntegerField()
    sugars = forms.IntegerField()

    class Meta():
        model = Food
        fields = ('name', 'category', 'calories', 'sodium', 'protien', 'carbs', 'fats', 'sugars')