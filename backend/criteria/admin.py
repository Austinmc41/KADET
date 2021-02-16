from django.contrib import admin
from .models import Criteria

# added for this project
@admin.register(Criteria)
class SchedulerAdmin(admin.ModelAdmin):  
    list_display = ("RotationType", "MinResident", "MaxResident")
