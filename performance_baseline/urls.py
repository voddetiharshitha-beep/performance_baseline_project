from django.urls import path
from api import views
urlpatterns = [
    path("api/login/", views.login_api),
    path("api/drivers/location/", views.driver_location),
    path("api/drivers/nearby/", views.nearby_drivers),
    path("api/rides/", views.create_ride),
    path("api/rides/<int:ride_id>/", views.ride_details),
    path("api/rides/history/", views.ride_history),
    path("api/notifications/", views.notifications),
]
