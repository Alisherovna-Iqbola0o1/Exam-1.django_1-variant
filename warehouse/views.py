from django.http import JsonResponse
from .models import WarehouseProduct

# Create your views here.

def stock(request):
    total = sum(i.quantity for i in WarehouseProduct.objects.all())
    return JsonResponse({"stock": total})
