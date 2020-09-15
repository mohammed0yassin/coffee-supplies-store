from django.db import models

class CoffeePod(models.Model):
    largePod = 'COFFEE_POD_LARGE'
    smallPod = 'COFFEE_POD_SMALL'
    espressoPod = 'ESPRESSO_POD'
    PRODUCT_TYPE_CHOICES = (
        (largePod, 'Large Pod'),
        (smallPod, 'Small Pod'),
        (espressoPod, 'Espresso Pod'),
    )
    product_type =  models.CharField(max_length=20,
                                      choices=PRODUCT_TYPE_CHOICES,
                                      default=largePod)

    flavor_vanilla = 'COFFEE_FLAVOR_VANILLA'
    flavor_caramel = 'COFFEE_FLAVOR_CARAMEL'
    flavor_psl = 'COFFEE_FLAVOR_PSL'
    flavor_mocha = 'COFFEE_FLAVOR_MOCHA'
    flavor_hazelnut = 'COFFEE_FLAVOR_HAZELNUT'
    FLAVOR_CHOICES = (
        (flavor_vanilla, 'vanilla'),
        (flavor_caramel, 'caramel'),
        (flavor_psl, 'psl'),
        (flavor_mocha, 'mocha'),
        (flavor_hazelnut, 'hazelnut'),
    )
    coffee_flavor = models.CharField(max_length=30,
                                      choices=FLAVOR_CHOICES,
                                      default=flavor_vanilla)

    one_dozen = '12'
    three_dozen = '36'
    five_dozen = '60'
    seven_dozen = '84'
    PACK_SIZE_CHOICES = (
        (one_dozen, '1 dozen'),
        (three_dozen, '3 dozen'),
        (five_dozen, '5 dozen'),
        (seven_dozen, '7 dozen'),
    )
    pack_size = models.CharField(max_length=7,
                                      choices=PACK_SIZE_CHOICES,
                                      default=one_dozen)