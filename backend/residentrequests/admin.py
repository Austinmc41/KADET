from django.contrib import admin
from .models import ResidentRequests

# added for this project
@admin.register(ResidentRequests)
class RequestsAdmin(admin.ModelAdmin):  
    list_display = ("email", "requestOne", "requestTwo", "requestThree")
