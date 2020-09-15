from django.shortcuts import render
from .models import CoffeeMachine
from .forms import MyModelForm

def show_machines(request):
    machines = CoffeeMachine.objects.all()
    return render(request, 'coffee_machines/machines.html', {'coffee_machines': machines})