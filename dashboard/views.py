from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q

from cities.models import City
from developments.models import Development, Enquiry
from .forms import CityForm, DevelopmentForm


def is_staff_or_superuser(user):
    return user.is_active and (user.is_staff or user.is_superuser)


@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_index(request):
    active_cities = City.objects.filter(is_active=True).count()
    active_developments = (
        Development.objects
        .filter(is_active=True)
        .count()
    )
    total_enquiries = Enquiry.objects.count()

    recent_enquiries = (
        Enquiry.objects
        .select_related("development")
        .order_by("-created_at")[:3]
    )

    return render(
        request,
        "dashboard/index.html",
        {
            "active_cities": active_cities,
            "active_developments": active_developments,
            "enquiries": recent_enquiries,
            "total_enquiries": total_enquiries,
        },
    )


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


@login_required
@user_passes_test(is_staff_or_superuser)
def development_list(request):
    q = request.GET.get("q", "").strip()
    status = request.GET.get("status", "")

    developments = Development.objects.select_related("city").order_by("name")

    if q:
        developments = developments.filter(
            Q(name__icontains=q) |
            Q(city__name__icontains=q) |
            Q(postcode__icontains=q)
        )

    if status == 'active':
        developments = developments.filter(is_active=True)
    elif status == 'inactive':
        developments = developments.filter(is_active=False)

    return render(
        request,
        "dashboard/developments/list.html",
        {
            "developments": developments,
            "q": q,
            "status": status,
        },
    )


@login_required
@user_passes_test(is_staff_or_superuser)
def development_toggle_active(request, pk):
    if request.method != "POST":
        return redirect("dashboard:developments_list")

    development = get_object_or_404(Development, pk=pk)

    # Toggle active state
    development.is_active = not development.is_active
    development.save()

    # Preserve filters/search
    query_string = request.META.get("QUERY_STRING", "")
    redirect_url = reverse("dashboard:developments_list")

    if query_string:
        return redirect(f"{redirect_url}?{query_string}")

    return redirect(redirect_url)


@login_required
@user_passes_test(is_staff_or_superuser)
def create_development(request):
    if request.method == "POST":
        development_form = DevelopmentForm(request.POST)

        if development_form.is_valid():
            development_form.save()
            return redirect("dashboard:developments_list")
    else:
        development_form = DevelopmentForm()

    return render(
        request,
        "dashboard/developments/create.html",
        {
            "development_form": development_form,
        }
    )


@login_required
@user_passes_test(is_staff_or_superuser)
def edit_development(request, pk):
    development = get_object_or_404(Development, pk=pk)

    if request.method == "POST":
        development_form = DevelopmentForm(
            request.POST,
            request.FILES,
            instance=development,
        )

        if development_form.is_valid():
            development_form.save()
            return redirect("dashboard:developments_list")
    else:
        development_form = DevelopmentForm(instance=development)

    return render(
        request,
        "dashboard/developments/edit.html",
        {
            "development_form": development_form,
            "development": development,
        },
    )


@login_required
@user_passes_test(is_staff_or_superuser)
def development_detail(request, pk):
    development = get_object_or_404(Development, pk=pk)
    return render(
        request,
        "dashboard/developments/detail.html",
        {"development": development}
    )


@login_required
@user_passes_test(is_staff_or_superuser)
def enquiries_list(request):
    enquiries = Enquiry.objects.select_related("development")

    return render(
        request,
        "dashboard/enquiries/list.html",
        {
            "enquiries": enquiries,
        }
    )


@login_required
@user_passes_test(is_staff_or_superuser)
def enquiry_detail(request, pk):
    enquiry = get_object_or_404(Enquiry, pk=pk)

    return render(
        request,
        "dashboard/enquiries/detail.html",
        {
            "enquiry": enquiry,
        }
    )
