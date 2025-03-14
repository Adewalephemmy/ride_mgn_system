from django.db import models

# Create your models here.
class Driver(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    location = models.JSONField()  # Store (latitude, longitude)
    rating = models.FloatField()
    preferences = models.JSONField()  # { "smoking": False, "music": True, "pets": False }
    available = models.BooleanField(default=True)

class Passenger(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    pickup_location = models.JSONField()  # (latitude, longitude)
    destination = models.JSONField()  # (latitude, longitude)
    preferences = models.JSONField()    
    