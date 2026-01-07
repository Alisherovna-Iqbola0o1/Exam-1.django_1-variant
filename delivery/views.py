from django.shortcuts import render
from django.http import JsonResponse
from .models import Delivery
# Create your views here.


def deliveries(request):
    count = Delivery.objects.count()
    return JsonResponse({"count": count})
