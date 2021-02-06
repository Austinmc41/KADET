from django.contrib import admin
from .models import Criteria

# Register your models here.


class SchedulerAdmin(admin.ModelAdmin):  # add this
    list_display = ("RotationType", "TypeAmount")  # add this


# Register your models here.
admin.site.register(Criteria, SchedulerAdmin)  # add this
