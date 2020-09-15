from django.forms import ModelForm
from .models import CoffeeMachine

class MyModelForm(ModelForm):
    class Meta:
        model = CoffeeMachine
        fields = ['product_type', 'water_line']