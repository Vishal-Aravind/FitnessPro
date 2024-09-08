#myapp/views.py

from django.shortcuts import render, redirect
from .models import Food,Consume
from datetime import date
# Create your views here.
def index(request):
    today = date.today()

    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')
        if food_consumed:
            food_item = Food.objects.get(name=food_consumed)
            user = request.user

            # Create a new Consume entry
            consume = Consume(user=user, food_consumed=food_item, date=today)
            consume.save()

        return redirect('index')  # Redirect to avoid form resubmission on page refresh

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user, date=today)

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('index')
    return render(request,'myapp/delete.html')
