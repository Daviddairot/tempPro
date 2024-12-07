from django.db import models

class Temperatures(models.Model):  # Renamed class for clarity
    date = models.DateField()  # Manual entry of date
    time=models.TimeField(default="00:00:00")
    temperature1 = models.IntegerField(null=True, blank=True, default=0)
    humidity1 = models.IntegerField(null=True, blank=True, default=0)
    temperature2 = models.IntegerField(null=True, blank=True, default=0)
    humidity2 = models.IntegerField(null=True, blank=True, default=0)
    temperature3 = models.IntegerField(null=True, blank=True, default=0)
    humidity3 = models.IntegerField(null=True, blank=True, default=0)
    temperature4 = models.IntegerField(null=True, blank=True, default=0)
    humidity4 = models.IntegerField(null=True, blank=True, default=0)
    temperature5 = models.IntegerField(null=True, blank=True, default=0)
    humidity5 = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        # String representation includes both date and time for clarity
        return f"{self.date.strftime('%Y-%m-%d')} {self.time.strftime('%H:%M:%S')}"
