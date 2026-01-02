from django.shortcuts import render
from cities.models import City


# Create your views here.
def city_list(request):
    cities = City.objects.filter(is_active=True).order_by("name")
    return render(request, "cities/city_list.html", {"cities": cities})
