from rest_framework import serializers
from .models import CoffeePod

class CoffeePodSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoffeePod
        fields =['id', 'product_type', 'coffee_flavor', 'pack_size']

