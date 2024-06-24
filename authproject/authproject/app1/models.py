from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True )
    continent = models.CharField(max_length=50, blank=False, null=False )
    population = models.IntegerField()

    def __str__(self):
        return self.name
