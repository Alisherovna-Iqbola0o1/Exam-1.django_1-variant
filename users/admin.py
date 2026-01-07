from django.contrib import admin
from .models import User, Client, LeadStatus, Log
# Register your models here.

admin.site.register(User)
admin.site.register(Client)
admin.site.register(LeadStatus)
admin.site.register(Log)
