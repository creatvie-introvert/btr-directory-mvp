"""
Views for the core app.

This module contains the homepage view.
"""

from django.shortcuts import render
from django.db.models import Q

from cities.models import City
from developments.models import Development


def home(request):
    """
    Shows the homepage.

    Loads active cities that are marked to appear on the homepage.
    """
    cities = City.objects.filter(is_active=True, show_on_homepage=True)
    return render(request, "core/home.html", {"cities": cities})


def search(request):
    """
    Shows the search result page.

    Reads the query from the URL (?q=...) and returns matching active
    devlopments.
    """
    query = request.GET.get("q", "").strip()

    developments = Development.objects.none()
    cities = City.objects.none()

    if query:
        developments = (
            Development.objects.filter(is_active=True)
            .select_related("city")
            .filter(
                Q(name__icontains=query)
                | Q(area_name__icontains=query)
                | Q(postcode__icontains=query)
                | Q(city__name__icontains=query)
            )
            .order_by("name")
            .distinct()
        )

        cities = (
            City.objects.filter(is_active=True)
            .filter(
                Q(name__icontains=query)
                | Q(slug__icontains=query)
            )
            .order_by("name")
            .distinct()
        )

    return render(
        request,
        "core/search_results.html",
        {
            "query": query,
            "developments": developments,
            "cities": cities,
        }
    )
