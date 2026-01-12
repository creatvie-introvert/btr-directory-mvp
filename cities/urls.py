"""
URL routes for the cities pages.

- /cities/ shows the list of cities
- /cities/<slug>/ shows one city and its developments
"""

from django.urls import path

from . import views

app_name = "cities"

urlpatterns = [
    path("", views.city_list, name="list"),
    path("<slug:slug>/", views.city_detail, name="detail"),
]
