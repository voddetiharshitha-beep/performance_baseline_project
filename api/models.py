from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)

class Driver(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(default=17.385)
    longitude = models.FloatField(default=78.4867)
    available = models.BooleanField(default=True)

class Ride(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, null=True, blank=True, on_delete=models.SET_NULL)
    pickup = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    status = models.CharField(max_length=30, default="requested")
    fare = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
