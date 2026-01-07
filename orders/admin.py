from django.contrib import admin
from .models import (
    Order,
    OrderProduct,
    OrderStatus,
    OrderCancelled,
    OrderCancelledStatus
)


# Register your models here.
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(OrderStatus)
admin.site.register(OrderCancelled)
admin.site.register(OrderCancelledStatus)
