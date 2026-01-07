from django.urls import path
from .views import deliveries

urlpatterns = [
    path("", deliveries),
]
