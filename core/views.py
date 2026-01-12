"""
Views for the core app.

This module contains the homepage view.
"""

from django.shortcuts import render

from cities.models import City


def home(request):
    """
    Shows the homepage.

    Loads active cities that are marked to appear on the homepage.
    """
    cities = City.objects.filter(is_active=True, show_on_homepage=True)
    return render(request, "core/home.html", {"cities": cities})
