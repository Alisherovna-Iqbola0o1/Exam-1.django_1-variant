from django.contrib import admin
from .models import Delivery, DeliveryGroup, DeliveryWorkDay, DeliveryWalletLog

# Register your models here.

admin.site.register(Delivery)
admin.site.register(DeliveryGroup)
admin.site.register(DeliveryWorkDay)
admin.site.register(DeliveryWalletLog)
