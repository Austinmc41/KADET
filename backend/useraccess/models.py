from django.db import models
from django.contrib.auth.models import AbstractUser

class SchedulerUser(AbstractUser):
    ACCESS_CHOICES = (
        ('NA', 'not applicable'),
        ('PGY1', 'year 1 resident'),
        ('PGY2', 'year 2 resident'),
        ('PGY3', 'year 3 resident'),
        ('PGY4', 'year 4 resident'),
        ('PGY5', 'year 5 resident'),
    )
    AccessLevel = models.CharField(
        max_length=5,
        choices=ACCESS_CHOICES,
    )
    email = models.EmailField(max_length=254, unique=True, primary_key=True)

    ResidentSchedule = models.JSONField(blank=True, null=True, default=dict)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email