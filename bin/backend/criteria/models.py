from django.db import models

class Criteria(models.Model):
    RotationType = models.CharField(max_length=120)
    MinResident = models.PositiveIntegerField()
    MaxResident = models.PositiveIntegerField()

    def __str__(self):
        return self.RotationType
