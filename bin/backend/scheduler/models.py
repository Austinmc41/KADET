from django.db import models
from django.urls import reverse

# Create your models here.

# add this
class Criteria(models.Model):
    RotationType = models.CharField(max_length=120)
    TypeAmount = models.PositiveIntegerField()

    def __str__(self):
        return self.RotationType

    def get_absolute_url(self):
        return reverse('criteria-list', kwargs={})