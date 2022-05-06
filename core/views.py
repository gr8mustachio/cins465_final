from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core.forms import JoinForm, LoginForm
from food.models import Food, FoodCategory
from workouts.models import Workout, MuscleGroup
# Create your views here.

@login_required(login_url='/login/')
def main(request):
    calsBurned = 0
    calGoal = 350
    name, calories, sodium, carbs, = [], [], [], []
    fats, sugars, date = [], [], []
    workout_data = Workout.objects.filter(user=request.user)
    food_data = Food.objects.filter(user=request.user)
    for data in workout_data:
        calsBurned += data.calsburned
    for data in food_data:
        print(data.name)
        #name2 = data.name
        name.append(data.name)
        calories.append(data.calories)
        sodium.append(data.sodium)
        carbs.append(data.carbs)
        fats.append(data.fats)
        sugars.append(data.sugars)
    context = {
        'calsBurned': calsBurned,
        'calGoal': calGoal,
        'name': name,
        'calories': calories,
        'sodium': sodium,
        'carbs': carbs,
        'fats': fats,
        'sugars': sugars
    }
    print(name, calories, sodium, carbs, fats, sugars)
    #print(name2)
    return render(request, 'core/home.html', context)
    #return HttpResponse("Dashboard Home Page")


def about(request):
    return render(request, 'core/about.html')

def user_login(request):
    #return HttpResponse("Login Page")
    if(request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if(login_form.is_valid()):
            #get username and password given
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            #django auth function
            user = authenticate(username=username, password=password)
            #if user exists
            if user:
                #check if is_active
                if(user.is_active):
                    #log them in
                    login(request,user)
                    #send to homepage
                    return redirect("/")
                    #return render(request)
                else:
                    #account not active
                    return HttpResponse("Your account is not active.")
            else:
                print("someone tried to login and failed")
                print("they used username: {} and password {}".format(username,password))
                return render(request, 'core/login.html', {"login_form": LoginForm})
    else:
                #nothing provided
        return render(request, 'core/login.html', {'login_form': LoginForm})


@login_required(login_url='/login/')
def user_logout(request):
    #log out user
    logout(request)
    #return to homepage
    return redirect("/")

def join(request):
    #return HttpResponse("Join Page")
    if(request.method == 'POST'):
        join_form = JoinForm(request.POST)
        if(join_form.is_valid()):
            #save the data to DB
            user = join_form.save()
            #encrypt Password
            user.set_password(user.password)
            #save encrypted password to db
            user.save()
            #success, back to homepage
            return redirect("/")
        else:
            #form is invalid, print error to console
            page_data = { "join_form": join_form }
            return render(request, 'core/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'core/join.html', page_data)
    