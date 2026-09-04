import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "performance_baseline.settings")
import django
django.setup()
from api.models import User, Driver, Ride, Notification
u, _ = User.objects.get_or_create(username="demo")
if Driver.objects.count() == 0:
    for i in range(10):
        Driver.objects.create(name=f"Driver {i+1}", latitude=17.385+i*0.001, longitude=78.4867+i*0.001)
d = Driver.objects.first()
if Ride.objects.count() == 0:
    for i in range(20):
        Ride.objects.create(user=u, driver=d, pickup=f"Pickup {i+1}", destination=f"Destination {i+1}", fare=200+i)
if Notification.objects.count() == 0:
    for i in range(20):
        Notification.objects.create(user=u, message=f"Ride notification {i+1}")
print("Seed data created.")
