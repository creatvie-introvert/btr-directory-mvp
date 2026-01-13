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

    min_beds = request.GET.get("min_beds")
    max_beds = request.GET.get("max_beds")
    min_rent = request.GET.get("min_rent")
    max_rent = request.GET.get("max_rent")

    min_beds = int(min_beds) if min_beds and min_beds.isdigit() else None
    max_beds = int(max_beds) if max_beds and max_beds.isdigit() else None
    min_rent = int(min_rent) if min_rent and min_rent.isdigit() else None
    max_rent = int(max_rent) if max_rent and max_rent.isdigit() else None

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

    if min_beds is not None:
        developments = developments.filter(max_bedrooms__gte=min_beds)

    if max_beds is not None:
        developments = developments.filter(min_bedrooms__lte=max_beds)

    if min_rent is not None:
        developments = developments.filter(rent_from_pcm__gte=min_rent)

    if max_rent is not None:
        developments = developments.filter(rent_from_pcm__lte=max_beds)    

    return render(
        request,
        "cities/city_detail.html",
        {"city": city, "developments": developments},
    )
