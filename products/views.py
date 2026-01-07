from django.http import JsonResponse
from .models import Product, Category, Color
from users.models import User
# Create your views here.


def create_product(request):
    seller = User.objects.first()
    category = Category.objects.first()
    color = Color.objects.first()

    product = Product.objects.create(
        name="Test Product",
        category=category,
        color=color,
        price=10000,
        seller=seller
    )

    return JsonResponse({
        "product_id": product.id
    })
