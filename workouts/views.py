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

@login_required(login_url='/login/')
def add(request):
    if(request.method == 'POST'):
        if('add' in request.POST):
            add_form = WorkoutForm(request.POST)
            if(add_form.is_valid()):
                workoutEntry = add_form.save(commit=False)
                workoutEntry.user = request.user
                workoutEntry.save()
                return redirect('/workouts/')
            else:
                context = {
                    'form_data': add_form
                }
                return render(request, 'workouts/add.html', context)
        else:
            #cancel
            return redirect('/workouts/')
    else:
        context = {
            'form_data': WorkoutForm()
        }
        return render(request, 'workouts/add.html', context)
    #return HttpResponse('add page')

@login_required(login_url='/login/')
def edit(request,id):
    if(request.method == 'GET'):
        #LOAD workout entry form with current model form
        workout = Workout.objects.get(id=id)
        form = WorkoutForm(instance=workout)
        context = { 'form_data': form }
        return render(request, 'workouts/edit.html', context)
    elif request.method == 'POST':
        if 'edit' in request.POST:
            form = WorkoutForm(request.POST)
            if form.is_valid():
                #Saving with commit=False gets you a model object,
                #then you can add your extra data and save it.
                workout = form.save(commit=False)
                workout.user = request.user
                workout.id = id
                workout.save()
                return redirect('/workouts/')
            else:
                context = {
                    'form_data': form,
                }
                return render(request, 'workouts/add.html', context)
        else:
            #cancel
            return redirect('/workouts/')
    #return HttpResponse('edit page')
