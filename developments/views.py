from django.shortcuts import render, get_object_or_404
from .models import Development, DevelopmentImage


# Create your views here.
def development_detail(request, slug):
    development = get_object_or_404(Development, slug=slug)

    images = DevelopmentImage.objects.filter(development=development).order_by("sort_order", "id")
    first_gallery = images.first()

    if development.cover_image:
        main_image = development.cover_image
        main_image_alt = first_gallery.alt_text or development.name
    elif images.exists():
        main_image = first_gallery.image
        main_image_alt = first_gallery.alt_text or development.name

    return render(
        request,
        "developments/development_detail.html",
        {
            "development": development,
            "images": images,
            "main_image": main_image,
            "main_image_alt": main_image_alt,
        },
    )
