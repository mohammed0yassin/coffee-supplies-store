from .models import CoffeeMachine
from rest_framework import viewsets
from .serializers import CoffeeMachineSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class CoffeeMachineMangement(viewsets.ModelViewSet):
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type', 'water_line', 'brand_model']

    def list(self, request, *args, **kwargs):
        response = super(CoffeeMachineMangement, self).\
            list(self, request, *args, **kwargs)
        # replace the response data with its equvilant SKU    
        for idx in range(len(response.data)):
            response.data[idx] = self.generate_sku(response.data[idx])
        return response    

    def generate_sku(self, data):
        """Generate the SKU"""
        product_type = data['product_type']
        brand_model = data['brand_model']
        water_line = data['water_line']

        if product_type == CoffeeMachine.largeMachine:
            product_type_code = 'CM1'
        elif product_type == CoffeeMachine.smallMachine:
            product_type_code = 'CM0'
        elif product_type == CoffeeMachine.espressoMachine:
            product_type_code = 'EM0'

        if brand_model == CoffeeMachine.baseModel:
            brand_model_code = '1'
        elif brand_model == CoffeeMachine.premiumModel:
            brand_model_code = '2'
        elif brand_model == CoffeeMachine.deluxeModel:
            brand_model_code = '3'
 
        if water_line is False:
            water_line_code = '0'
        elif water_line is True:
            water_line_code = '1'
 
        sku = {
            'SKU' : '{}'.format(product_type_code + water_line_code + brand_model_code) 
            }

        return sku