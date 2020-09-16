from django.urls import path, include
from coffee_machines import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.CoffeeMachineMangement)

urlpatterns = [
    path('machine/', include(router.urls)),
]
