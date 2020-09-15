from django.urls import path, include
from coffee_pods import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.CoffeePodMangement)

urlpatterns = [
    path('pods/', include(router.urls)),
]

