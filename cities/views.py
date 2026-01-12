"""
Views for listing cities and showing developments within a city.
Adds bedroom-range summary data to development cards using UnitType records.
"""

from django.db.models import Min, Max, Q
from django.shortcuts import render, get_object_or_404

from cities.models import City


def city_list(request):
    """
    Shows the cities index page.

    Only active cities are listed, ordered alphabetically.
    """
    cities = City.objects.filter(is_active=True).order_by("name")
    return render(request, "cities/city_list.html", {"cities": cities})


def city_detail(request, slug):
    """
    Shows one city page with its active developments.

    Adds min/max bedroom count per development (based on available unit types)
    so the listing cards can show a bedroom range.
    """
    city = get_object_or_404(City, slug=slug, is_active=True)

    # Add bedroom range per development for the listing cards
    developments = (
        city.developments.filter(is_active=True)
        .annotate(
            min_bedrooms=Min(
                "unit_types__bedrooms",
                filter=Q(unit_types__is_available=True),
            ),
            max_bedrooms=Max(
                "unit_types__bedrooms",
                filter=Q(unit_types__is_available=True),
            ),
        )
        .order_by("name")
    )

    return render(
        request,
        "cities/city_detail.html",
        {"city": city, "developments": developments},
    )
