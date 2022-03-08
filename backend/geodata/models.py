from django.db import models
from django.forms import CharField
from django.urls import reverse

# Create your models here.
class GeoData(models.Model):
    name = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    geolocation = models.TextField()
    approved = models.BooleanField(default=False)

    @property
    def approve_url(self):
        return reverse('geodata_approve_view', args=[self.id])
