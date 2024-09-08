#views.py/dietwork

from django.shortcuts import render
from .models import DietPlan, WorkoutPlan
from django.contrib.auth.decorators import login_required

@login_required
def diet(request):
    user = request.user
    diet_plans = DietPlan.objects.filter(user=user).order_by('-date')  # Get all diet plans for the user
    context = {
        'diet_plans': diet_plans,
    }
    return render(request, 'dietwork/diet.html', context)

@login_required
def workout(request):
    user = request.user
    workout_plans = WorkoutPlan.objects.filter(user=user).order_by('-date')  # Get all workout plans for the user
    context = {
        'workout_plans': workout_plans,
    }
    return render(request, 'dietwork/workout.html', context)
