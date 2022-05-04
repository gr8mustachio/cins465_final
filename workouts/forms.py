from django import forms
from workouts.models import MuscleGroup, Workout

class WorkoutForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    musclegroup = forms.ModelChoiceField(queryset=MuscleGroup.objects.all())
    date = forms.DateField()
    sets = forms.IntegerField(required=False)
    reps = forms.IntegerField(required=False)
    distance = forms.DecimalField(required=False)
    duration = forms.DurationField()
    calsburned = forms.IntegerField()
    heartAvg = forms.IntegerField()

    class Meta:
        model = Workout
        fields = ('name', 'musclegroup', 'sets', 'reps', 'distance', 'duration', 'calsburned', 'heartAvg')
        labels = {
            'name': ('Writer'),
        }