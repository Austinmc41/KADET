from django.contrib import admin
from .models import Criteria

@admin.register(Criteria)
class SchedulerAdmin(admin.ModelAdmin):  
    list_display = ("RotationType", "MinResident", "MaxResident")
