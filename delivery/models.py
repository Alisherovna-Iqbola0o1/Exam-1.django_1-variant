from django.db import models
from users.models import User
# Create your models here.


class DeliveryGroup(models.Model):
    name = models.CharField(max_length=100)


class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(DeliveryGroup, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)


class DeliveryWorkDay(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    date = models.DateField()


class DeliveryWalletLog(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
