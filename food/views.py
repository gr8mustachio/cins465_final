
from unicodedata import category
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from food.models import FoodCategory, Food
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
        #xMax = maximum amount allowed
        #xMin = minimum amount allowed
        #xGoal = general goal
    if(request.method == 'GET' and 'delete' in request.GET):
        print('fuck')
        id=request.GET['delete']
        print(id)
        Food.objects.filter(id=id).delete()
        return redirect("/food/")
    else:
        food_data = Food.objects.filter(user=request.user)
        #have the goals be as a 5x1 table with percentages
        calorieGoal = 2000
        sodMax = 2300
        protMin = 60
        carbGoal = 275
        fatGoal = 60.5
        sugMax = 36

        sodium = 0
        calories = 0
        protien = 0
        carbs = 0
        fats = 0
        sugars = 0
        for food in food_data:
            calories += food.calories
            sodium += food.sodium
            protien += food.protien
            carbs  += food.carbs
            fats  += food.fats 
            sugars  += food.sugars
        sodiumPerc = (int)((sodium / sodMax) * 100)
        caloriePerc = (int)((calories / calorieGoal) * 100)
        protienPerc = (int)((protien / protMin) * 100)
        carbPerc = (int)((carbs / carbGoal) * 100)
        fatPerc = (int)((fats / fatGoal) * 100)
        sugarPerc = (int)((sugars / sugMax) * 100)
        context = {
            'food_data' : food_data,
            'sodiumPerc': sodiumPerc,
            'caloriePerc': caloriePerc,
            'protienPerc': protienPerc,
            'carbPerc' : carbPerc,
            'fatPerc': fatPerc,
            'sugarPerc': sugarPerc
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

@login_required(login_url='/login/')
def edit(request, id):
    if(request.method=='GET'):
        #load task entry form with current model form
        foodEntry = Food.objects.get(id=id)
        form = FoodForm(instance=foodEntry)
        context = { 'form_data': form }
        return render(request, 'food/edit.html', context)
    elif (request.method == 'POST'):
        if('edit' in request.POST):
            form = FoodForm(request.POST)
            if(form.is_valid()):
                #Saving with commit=False gets you a model object,
                #then you can add your extra data and save it.
                foodEntry = form.save(commit=False)
                foodEntry.user = request.user
                foodEntry.id = id
                foodEntry.save()
                return redirect('/food/')
            else:
                context = {
                    'form_data' : form,
                }
                return render(request, 'food/add.html', context)
        else:
            #cancel
            return redirect('/food/')

    #return HttpResponse("edit page")