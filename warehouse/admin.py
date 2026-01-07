from django.contrib import admin
from .models import Warehouse, WarehouseProduct, WarehouseHistory

# Register your models here.

admin.site.register(Warehouse)
admin.site.register(WarehouseProduct)
admin.site.register(WarehouseHistory)
