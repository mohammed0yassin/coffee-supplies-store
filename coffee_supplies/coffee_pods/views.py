from .models import CoffeePod
from rest_framework import viewsets
from .serializers import CoffeePodSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CoffeePodMangement(viewsets.ModelViewSet):
    queryset = CoffeePod.objects.all()
    serializer_class = CoffeePodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type', 'coffee_flavor', 'pack_size']