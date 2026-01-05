from django.shortcuts import render, get_object_or_404
from .models import Development


# Create your views here.
def development_detail(request, slug):
    development = get_object_or_404(Development, slug=slug)
    return render(request, "developments/development_detail.html", {
            "development": development
        })
