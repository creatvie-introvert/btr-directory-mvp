from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q

from cities.models import City
from .forms import CityForm


def is_staff_or_superuser(user):
    return user.is_active and (user.is_staff or user.is_superuser)


@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_index(request):
    return render(request, "dashboard/index.html")


@login_required
@user_passes_test(is_staff_or_superuser)
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


@login_required
@user_passes_test(is_staff_or_superuser)
def city_toggle_active(request, city_id):
    if request.method != "POST":
        return redirect("dashboard:cities_list")

    city = get_object_or_404(City, id=city_id)

    # Toggle active state
    city.is_active = not city.is_active
    city.save()

    # Preserve filters/search
    query_string = request.META.get("QUERY_STRING", "")
    redirect_url = reverse("dashboard:cities_list")

    if query_string:
        return redirect(f"{redirect_url}?{query_string}")

    return redirect(redirect_url)


@login_required
@user_passes_test(is_staff_or_superuser)
def create_city(request):
    if request.method == "POST":
        city_form = CityForm(request.POST, request.FILES)

        if city_form.is_valid():
            city_form.save()
            return redirect("dashboard:cities_list")
    else:
        city_form = CityForm()

    return render(
        request,
        "dashboard/cities/create.html",
        {
            "city_form": city_form,
        }
    )


@login_required
@user_passes_test(is_staff_or_superuser)
def edit_city(request, city_id):
    city = get_object_or_404(City, id=city_id)

    if request.method == "POST":
        city_form = CityForm(request.POST, request.FILES, instance=city)

        if city_form.is_valid():
            city_form.save()
            return redirect("dashboard:cities_list")
    else:
        city_form = CityForm(instance=city)

    return render(
        request,
        "dashboard/cities/edit.html",
        {
            "city_form": city_form,
            "city": city,
        },
    )


@login_required
@user_passes_test(is_staff_or_superuser)
def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(
        request,
        "dashboard/cities/detail.html",
        {"city": city}
    )
