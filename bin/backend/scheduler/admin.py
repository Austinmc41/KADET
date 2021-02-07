from django.contrib import admin
from .models import Criteria

# Register your models here.


class SchedulerAdmin(admin.ModelAdmin):  
    list_display = ("RotationType", "TypeAmount")  


# Register your models here.
admin.site.register(Criteria, SchedulerAdmin)  
