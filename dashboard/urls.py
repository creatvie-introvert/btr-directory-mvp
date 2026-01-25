"""
URL routes for the dashboard app.
"""

from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard_index, name="index"),
    path("cities/", views.city_list, name="cities_list"),
    path(
        "cities/<int:city_id>/toggle-active",
        views.city_toggle_active,
        name="city_toggle_active",
    ),
]
