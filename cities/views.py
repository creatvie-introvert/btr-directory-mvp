from django.db.models import Min, Max, Q
from django.shortcuts import render, get_object_or_404
from cities.models import City


# Create your views here.
def city_list(request):
    cities = City.objects.filter(is_active=True).order_by("name")
    return render(request, "cities/city_list.html", {"cities": cities})


def city_detail(request, slug):
    city = get_object_or_404(City, slug=slug, is_active=True)

    developments = (
        city.developments.filter(is_active=True).annotate(
            min_bedrooms=Min(
                "unit_types__bedrooms",
                filter=Q(unit_types__is_available=True)
            ),
            max_bedrooms=Max(
                "unit_types__bedrooms",
                filter=Q(unit_types__is_available=True)
            ),
        )
        .order_by("name")
    )    

    return render(
        request, "cities/city_detail.html",
        {
            "city": city,
            "developments": developments,
        }
    )
