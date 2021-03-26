from django.db import models

class ResidentRequests(models.Model):
    email = models.EmailField()
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    requestOne = models.DateField(null=True, blank=True)
    requestTwo = models.DateField(null=True, blank=True)
    requestThree = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.firstName