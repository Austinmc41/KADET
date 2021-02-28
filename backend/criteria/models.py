from django.db import models

class Criteria(models.Model):
    YEAR_CHOICES = (
        ('0', 'not applicable'),
        ('1', 'First year'),
        ('2', 'Second year'),
        ('3', 'Third year'),
        ('4', 'Fourth year'),
        ('5', 'Fifth year'),
    )
    RotationType = models.CharField(max_length=120)
    MinResident = models.PositiveIntegerField()
    MaxResident = models.PositiveIntegerField()
    ResidentYear = models.CharField(
        max_length=1,
        choices=YEAR_CHOICES,
        default='1',
    )

    def __str__(self):
        return self.RotationType
