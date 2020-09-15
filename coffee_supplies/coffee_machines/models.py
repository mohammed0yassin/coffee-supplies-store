from django.db import models

class CoffeMachine(models.Model):
    largeMachine = 'COFFEE_MACHINE_LARGE'
    smallMachine = 'COFFEE_MACHINE_SMALL'
    espressoMachine = 'ESPRESSO_MACHINE'
    PRODUCT_TYPE_CHOICES = (
        (largeMachine, 'Large Machine'),
        (smallMachine, 'Small Machine'),
        (espressoMachine, 'Espresso Machine'),
    )

    product_type =  models.CharField(max_length=20,
                                      choices=PRODUCT_TYPE_CHOICES,
                                      default=largeMachine)

    water_line = models.BooleanField(default=False)