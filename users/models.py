from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin"
        SELLER = "seller"
        DELIVERY = "delivery"
        CLIENT = "client"

    role = models.CharField(max_length=20, choices=Role.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LeadStatus(models.Model):
    name = models.CharField(max_length=100)


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clients")
    status = models.ForeignKey(LeadStatus, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
