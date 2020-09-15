from .models import CoffeeMachine
from rest_framework import viewsets
from .serializers import CoffeeMachineSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CoffeeMachineMangement(viewsets.ModelViewSet):
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type', 'water_line', 'brand_model']