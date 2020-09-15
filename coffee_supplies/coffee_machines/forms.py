from django.forms import ModelForm
from .models import CoffeMachine

class MyModelForm(ModelForm):
    class Meta:
        model = CoffeMachine
        fields = ['product_type', 'water_line']