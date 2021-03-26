from django.db import models

class Criteria(models.Model):
    YEAR_CHOICES = (
        ('NA', 'not applicable'),
        ('PGY1', 'year 1 resident'),
        ('PGY2', 'year 2 resident'),
        ('PGY3', 'year 3 resident'),
        ('PGY4', 'year 4 resident'),
        ('PGY5', 'year 5 resident'),
    )
    RotationType = models.CharField(max_length=120)
    StartRotation = models.DateField(null=True, blank=True)
    EndRotation = models.DateField(null=True, blank=True)
    MinResident = models.PositiveIntegerField()
    MaxResident = models.PositiveIntegerField()
    Overnight = models.BooleanField(default=False)
    Essential = models.BooleanField(default=False)
    ResidentYear = models.CharField(
        max_length=5,
        choices=YEAR_CHOICES,
        default=None,
    )

    def __str__(self):
        return self.RotationType