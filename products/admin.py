from django.contrib import admin
from .models import Category, Color, Product, ComboProduct, SellerWalletLog
# Register your models here.

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(ComboProduct)
admin.site.register(SellerWalletLog)
