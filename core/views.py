from django.shortcuts import render
from cities.models import City


# Create your views here.
def home(request):
    cities = City.objects.filter(is_active=True, show_on_homepage=True)
    return render(request, "core/home.html", {"cities": cities})
