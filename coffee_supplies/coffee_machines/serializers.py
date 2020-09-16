from rest_framework import serializers
from .models import CoffeeMachine

class CoffeeMachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoffeeMachine
        fields =['id', 'product_type', 'brand_model', 'water_line']
