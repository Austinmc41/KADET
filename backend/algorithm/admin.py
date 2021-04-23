from django.contrib import admin
from .models import AlgorithmStatus

# added for this project
@admin.register(AlgorithmStatus)
class AlgorithmStatusAdmin(admin.ModelAdmin):  
    list_display = ("Status",)
