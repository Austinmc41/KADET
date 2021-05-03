from django.db import models
from useraccess.models import SchedulerUser

class ResidentRequests(models.Model):
    email = models.OneToOneField(
        SchedulerUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    requestOne = models.DateField(null=True, blank=True)
    requestTwo = models.DateField(null=True, blank=True)
    requestThree = models.DateField(null=True, blank=True)

    ResidentSchedule = models.JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return self.email