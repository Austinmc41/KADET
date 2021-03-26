from django.contrib import admin
from .models import SchedulerUser

class SchedulerAdmin(admin.ModelAdmin):
    model = SchedulerUser

admin.site.register(SchedulerUser, SchedulerAdmin)