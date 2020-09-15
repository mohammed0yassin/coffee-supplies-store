import os
from coffee_supplies.settings import BASE_DIR
from django.shortcuts import render
from .models import CoffeMachine
from .forms import MyModelForm
from django.views.generic.edit import CreateView



class CreateMyModelView(CreateView):
    model = CoffeMachine
    form_class = MyModelForm
    template_name = 'template.html'
    # success_url = 'coffee_supplies/success.html'