from django.contrib import admin
from .models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):  
    list_display = ("email", "name", "postGradLevel", "generatedSchedule", "blackoutRotations", "assignedRotations")
