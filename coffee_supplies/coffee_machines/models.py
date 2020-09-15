from django.db import models

class CoffeeMachine(models.Model):
    largeMachine = 'COFFEE_MACHINE_LARGE'
    smallMachine = 'COFFEE_MACHINE_SMALL'
    espressoMachine = 'ESPRESSO_MACHINE'
    PRODUCT_TYPE_CHOICES = (
        (largeMachine, 'Large Machine'),
        (smallMachine, 'Small Machine'),
        (espressoMachine, 'Espresso Machine'),
    )

    product_type = models.CharField(max_length=20,
                                      choices=PRODUCT_TYPE_CHOICES,
                                      default=largeMachine)

    baseModel = 'BASE_MODEL'
    premiumModel = 'PREMIUM_MODEL'
    deluxeModel = 'DELUXE_MODEL'
    BRAND_MODEL_CHOICES = (
        (baseModel, 'Base Model'),
        (premiumModel, 'Premium Model'),
        (deluxeModel, 'Deluxe Model'),
    )

    brand_model = models.CharField(max_length=20,
                                      choices=BRAND_MODEL_CHOICES,
                                      default=baseModel)

    water_line = models.BooleanField(default=False)
