from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q

from cities.models import City


def is_staff_or_superuser(user):
    return user.is_active and (user.is_staff or user.is_superuser)


@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_index(request):
    return render(request, "dashboard/index.html")


def city_list(request):
    q = request.GET.get("q", "").strip()

    cities = City.objects.all().order_by("name")

    if q:
        cities = cities.filter(
            Q(name__icontains=q) | Q(slug__icontains=q)
        )
    return render(
        request,
        "dashboard/cities/list.html",
        {
            "cities": cities,
            "q": q,
        },
    )
