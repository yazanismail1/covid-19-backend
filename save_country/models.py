from django.db import models

# Create your models here.
class Country(models.Model):
    Country = models.CharField(max_length=56)
    TotalConfirmed = models.TextField(max_length=56)
    TotalDeaths = models.TextField(max_length=56)
    TotalRecovered = models.TextField(max_length=56)
    Date = models.TextField(max_length=56)

    def __str__(self):
        return self.country