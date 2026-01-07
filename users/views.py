from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import User, Client, LeadStatus, Log


def create_client(request):
    user = User.objects.create_user(
        username="client1",
        password="12345678",
        role="client"
    )

    status = LeadStatus.objects.first()

    client = Client.objects.create(
        user=user,
        status=status
    )

    Log.objects.create(
        user=user,
        action="Client created"
    )

    return JsonResponse({
        "user_id": user.id,
        "client_id": client.id
    })
