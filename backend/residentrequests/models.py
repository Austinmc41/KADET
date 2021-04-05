from django.db import models
from useraccess.models import SchedulerUser

class ResidentRequests(models.Model):
    email = models.OneToOneField(
        SchedulerUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    requestOne = models.DateField()
    requestTwo = models.DateField()
    requestThree = models.DateField()

    def __str__(self):
        return self.email