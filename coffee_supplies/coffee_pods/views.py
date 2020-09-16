from .models import CoffeePod
from rest_framework import viewsets
from .serializers import CoffeePodSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CoffeePodMangement(viewsets.ModelViewSet):
    queryset = CoffeePod.objects.all()
    serializer_class = CoffeePodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type', 'coffee_flavor', 'pack_size']

    def list(self, request, *args, **kwargs):
        response = super(CoffeePodMangement, self).\
            list(self, request, *args, **kwargs)
        # replace the response data with its equvilant SKU    
        for idx in range(len(response.data)):
            response.data[idx] = self.generate_sku(response.data[idx])
        return response    

    def generate_sku(self, data):
        """Generate the SKU"""
        product_type = data['product_type']
        coffee_flavor = data['coffee_flavor']
        pack_size = data['pack_size']

        if product_type == CoffeePod.largePod:
            product_type_code = 'CP1'
        elif product_type == CoffeePod.smallPod:
            product_type_code = 'CP0'
        elif product_type == CoffeePod.espressoPod:
            product_type_code = 'EP0'

        if coffee_flavor == CoffeePod.flavor_vanilla:
            coffee_flavor_code = '0'
        elif coffee_flavor == CoffeePod.flavor_caramel:
            coffee_flavor_code = '1'
        elif coffee_flavor == CoffeePod.flavor_psl:
            coffee_flavor_code = '2'
        elif coffee_flavor == CoffeePod.flavor_mocha:
            coffee_flavor_code = '3'
        elif coffee_flavor == CoffeePod.flavor_hazelnut:
            coffee_flavor_code = '4'

        if pack_size == CoffeePod.one_dozen:
            pack_size_code = '0'
        elif pack_size == CoffeePod.three_dozen:
            pack_size_code = '3'
        elif pack_size == CoffeePod.five_dozen:
            pack_size_code = '5'
        elif pack_size == CoffeePod.seven_dozen:
            pack_size_code = '7'

 
        sku = product_type_code + coffee_flavor_code + pack_size_code

        return sku