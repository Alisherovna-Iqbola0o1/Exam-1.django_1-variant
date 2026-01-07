from django.db import models
from users.models import User
from products.models import Product

# Create your models here.


class OrderStatus(models.Model):
    name = models.CharField(max_length=100)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class OrderCancelledStatus(models.Model):
    name = models.CharField(max_length=100)


class OrderCancelled(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderCancelledStatus, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
