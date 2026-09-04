from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from .models import User, Driver, Ride, Notification

@csrf_exempt
def login_api(request):
    username = request.GET.get("username", "demo")
    user, _ = User.objects.get_or_create(username=username)
    return JsonResponse({"token": "demo-token", "user_id": user.id, "username": user.username})

def driver_location(request):
    driver_id = request.GET.get("driver_id")
    d = Driver.objects.get(id=driver_id) if driver_id else Driver.objects.first()
    if not d: return JsonResponse({"error": "driver not found"}, status=404)
    return JsonResponse({"driver_id": d.id, "latitude": d.latitude, "longitude": d.longitude})

def nearby_drivers(request):
    drivers = Driver.objects.filter(available=True)[:10]
    return JsonResponse({"drivers": list(drivers.values("id", "name", "latitude", "longitude"))})

@csrf_exempt
def create_ride(request):
    user = User.objects.first()
    driver = Driver.objects.filter(available=True).first()
    ride = Ride.objects.create(user=user, driver=driver, pickup="Pickup", destination="Destination", fare=250)
    return JsonResponse({"ride_id": ride.id, "status": ride.status, "fare": float(ride.fare)}, status=201)

def ride_details(request, ride_id):
    ride = Ride.objects.select_related("user", "driver").get(id=ride_id)
    return JsonResponse({"ride_id": ride.id, "status": ride.status, "pickup": ride.pickup,
                         "destination": ride.destination, "fare": float(ride.fare),
                         "driver": ride.driver.name if ride.driver else None})

def ride_history(request):
    rides = Ride.objects.order_by("-id")[:20]
    return JsonResponse({"rides": list(rides.values("id", "pickup", "destination", "status", "fare"))})

def notifications(request):
    user = User.objects.first()
    notes = Notification.objects.filter(user=user).order_by("-id")[:20]
    return JsonResponse({"notifications": list(notes.values("id", "message", "read"))})
