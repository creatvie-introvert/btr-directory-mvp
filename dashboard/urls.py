"""
URL routes for the dashboard app.
"""

from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard_index, name="index"),
    path("cities/", views.city_list, name="cities_list"),
    path("developments/", views.development_list, name="developments_list"),
    path(
        "cities/<int:city_id>/toggle-active/",
        views.city_toggle_active,
        name="city_toggle_active",
    ),
    path(
        "developments/<int:pk>/toggle-active/",
        views.development_toggle_active,
        name="development_toggle_active",
    ),
    path("cities/add/", views.create_city, name="cities_add"),
    path(
        "developments/add/",
        views.create_development,
        name="development_add",
    ),
    path(
        "cities/<int:city_id>/edit",
        views.edit_city,
        name="city_edit",
    ),
    path(
        "developments/<int:pk>/edit",
        views.edit_development,
        name="development_edit",
    ),
    path(
        "cities/<int:pk>/",
        views.city_detail,
        name="city_detail",
    ),
    path(
        "developments/<int:pk>/",
        views.development_detail,
        name="development_detail",
    ),
    path(
        "enquiries/",
        views.enquiries_list,
        name="enquiries_list",
    ),
]
