from django.db import models

class ResidentRequests(models.Model):
    email = models.EmailField()
    requestOne = models.DateField()
    requestTwo = models.DateField()
    requestThree = models.DateField()

    def __str__(self):
        return self.firstName