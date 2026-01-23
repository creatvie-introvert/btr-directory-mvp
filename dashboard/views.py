from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


def is_staff_or_superuser(user):
    return user.is_active and (user.is_staff or user.is_superuser)


@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_index(request):
    return render(request, "dashboard/index.html")
