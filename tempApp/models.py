from django.db import models

# Create your models here.
class Temperatures(models.Model):  # Class names should be capitalized by convention
    date = models.DateField()
    temperature1 = models.IntegerField(null=True, default=0)
    humidity1 = models.IntegerField(null=True, default=0)
    temperature2 = models.IntegerField(null=True, default=0)
    humidity2 = models.IntegerField(null=True, default=0)
    temperature3 = models.IntegerField(null=True, default=0)
    humidity3 = models.IntegerField(null=True, default=0)
    temperature4 = models.IntegerField(null=True, default=0)
    humidity4 = models.IntegerField(null=True, default=0)
    temperature5 = models.IntegerField(null=True, default=0)
    humidity5 = models.IntegerField(null=True, default=0)

    def __str__(self):
        # Converting date to string because date is a DateField, not string.
        return self.date.strftime('%Y-%m-%d')
