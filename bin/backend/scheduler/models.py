from django.db import models

# Create your models here.

# add this
class Criteria(models.Model):
    RotationType = models.CharField(max_length=120)
    TypeAmount = models.PositiveIntegerField()

    def __str__(self):
        return self.RotationType

    def get_RotationType(self):
        return self.RotationType

    def get_TypeAmount(self):
        return self.TypeAmount

    def set_RotationType(self, RotationType):
        self.RotationType = RotationType

    def set_TypeAmount(self, TypeAmount):
        self.TypeAmount = TypeAmount
