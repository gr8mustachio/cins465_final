from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from workouts.models import Workout, MuscleGroup
from workouts.forms import WorkoutForm
# Create your views here.
@login_required(login_url='/login/')
def main(request):
    if(MuscleGroup.objects.count() == 0):
        MuscleGroup(group = 'Biceps').save()
        MuscleGroup(group = 'Triceps').save()
        MuscleGroup(group = 'Deltoids').save()
        MuscleGroup(group = 'Quads').save()
        MuscleGroup(group = 'Hamstrings').save()
        MuscleGroup(group = 'Upper Back').save()
        MuscleGroup(group = 'Lower Back').save()
        MuscleGroup(group = 'Upper Chest').save()
        MuscleGroup(group = 'Lower Chest').save()
        MuscleGroup(group = 'Core').save()
        MuscleGroup(group = 'Cardio').save()
        MuscleGroup(group = 'Full Body').save()
    workout_data = Workout.objects.filter(user=request.user)
    context = {
        'workout_data': workout_data
    }
    return render(request, 'workouts/workouts.html', context)

def add(request):
    return HttpResponse('add page')

def edit(request,id):
    return HttpResponse('edit page')
