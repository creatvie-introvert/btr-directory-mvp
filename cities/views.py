"""
Views for listing cities and showing developments within a city.
Adds bedroom-range summary data to development cards using UnitType records.
"""

from django.db.models import Min, Max, Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

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
    developments = city.developments.filter(is_active=True)

    # Filter developments by matching available unit types
    unit_filters = Q(unit_types__is_available=True)

    if min_beds is not None:
        unit_filters &= Q(unit_types__bedrooms__gte=min_beds)

    if max_beds is not None:
        unit_filters &= Q(unit_types__bedrooms__lte=max_beds)

    if min_rent is not None:
        unit_filters &= Q(unit_types__rent_from_pcm__gte=min_rent)

    if max_rent is not None:
        unit_filters &= Q(unit_types__rent_from_pcm__lte=max_rent)

    filters_active = any(v is not None for v in [min_beds, max_beds, min_rent, max_rent])

    # Only apply unit-type filtering if at least 1 filter selected by the user
    if filters_active:
        developments = developments.filter(unit_filters).distinct()

    annotations = {
        "min_bedrooms": Min(
            "unit_types__bedrooms",
            filter=Q(unit_types__is_available=True)
        ),
        "max_bedrooms": Max(
            "unit_types__bedrooms",
            filter=Q(unit_types__is_available=True)
        ),
    }

    if filters_active:
        annotations["card_rent_from_pcm"] = Min(
            "unit_types__rent_from_pcm",
            filter=unit_filters,
        )

    developments = developments.annotate(**annotations).order_by("name")

    page_number = request.GET.get("page")
    paginator = Paginator(developments, 9)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "cities/city_detail.html",
        {
            "city": city,
            "page_obj": page_obj,
            "developments": page_obj,
        }
    )
