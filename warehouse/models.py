from django.db import models
from products.models import Product
# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(max_length=100)


class WarehouseProduct(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class WarehouseHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
