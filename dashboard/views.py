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
    status = request.GET.get("status", "")
    homepage = request.GET.get("homepage", "")

    cities = City.objects.all().order_by("name")

    if q:
        cities = cities.filter(
            Q(name__icontains=q) | Q(slug__icontains=q)
        )

    if status == 'active':
        cities = cities.filter(is_active=True)
    elif status == 'inactive':
        cities = cities.filter(is_active=False)

    if homepage == 'yes':
        cities = cities.filter(show_on_homepage=True)
    elif homepage == 'no':
        cities = cities.filter(show_on_homepage=False)

    return render(
        request,
        "dashboard/cities/list.html",
        {
            "cities": cities,
            "q": q,
            "status": status,
            "homepage": homepage,
        },
    )
