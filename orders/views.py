from django.shortcuts import render
from django.http import JsonResponse
from .models import Order, OrderProduct, OrderStatus
from users.models import User
from products.models import Product
# Create your views here.


def create_order(request):
    user = User.objects.first()
    status = OrderStatus.objects.first()

    order = Order.objects.create(
        user=user,
        status=status
    )

    product = Product.objects.first()

    OrderProduct.objects.create(
        order=order,
        product=product,
        quantity=2
    )

    return JsonResponse({
        "order_id": order.id
    })
