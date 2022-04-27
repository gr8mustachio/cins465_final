import re
from unicodedata import category
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from food.models import FoodCategory, FoodItem
from food.forms import FoodForm
# Create your views here.

@login_required(login_url='/login/')
def main(request):
    if(FoodCategory.objects.count() == 0):
        FoodCategory(category = 'Grains').save()
        FoodCategory(category = 'Fats').save()
        FoodCategory(category = 'Protien').save()
        FoodCategory(category = 'Dairy').save()
        FoodCategory(category = 'Oils').save()
        FoodCategory(category = 'Sweets').save()
    if(request.method == 'GET' and 'DELETE' in request.GET):
        id=request.GET['delete']
        FoodItem.objects.filter(id=id).delete()
        return redirect('/food/')
    else:
        food_data = FoodItem.objects.filter(user=request.user)
        context = {
            'food_data' : food_data
        }
        return render(request, 'food/food.html', context)
    return render(request, 'food/food.html')

@login_required(login_url='/login/')
def add(request):
    if(request.method == 'POST'):
        if('add' in request.POST):
            add_form = FoodForm(request.POST)
            if(add_form.is_valid()):
                foodEntry = add_form.save(commit=False)
                foodEntry.user = request.user
                foodEntry.save()
                return redirect('/food/')
            else:
                context = {
                    'form_data': add_form
                }
                return render(request, 'food/add.html', context)
        else:
            #cancel
            return redirect('/food/')
    else:
        context = {
            'form_data' : FoodForm()
        }
        return render(request, 'food/add.html', context)