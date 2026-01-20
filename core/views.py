"""
Views for the core app.

This module contains the homepage view and static page views.
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
        # TODO: consider pagiation for larger search results
        developments = (
            Development.objects.filter(is_active=True)
            .select_related("city")
            .filter(
                Q(name__icontains=query)
                | Q(area_name__icontains=query)
                | Q(postcode__icontains=query)
                | Q(city__name__icontains=query)
            )
            .order_by("id")
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


def what_is_btr(request):
    """Shows the What is BTR? page"""
    return render(request, "core/what_is_btr.html")


def about(request):
    """Shows the About page"""
    return render(request, "core/about.html")


def disclaimer(request):
    """Shows the Disclaimer page"""
    return render(request, "core/disclaimer.html")


def accessibility_statement(request):
    """Shows the Accessibilty Statement"""
    return render(request, "core/accessibility_statement.html")
