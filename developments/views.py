from django.shortcuts import render, get_object_or_404
from .models import Development, DevelopmentImage


# Create your views here.
def development_detail(request, slug):
    development = get_object_or_404(Development, slug=slug)

    images = DevelopmentImage.objects.filter(development=development).order_by("sort_order", "id")
    first_gallery = images.first()

    unit_types = development.unit_types.order_by("bedrooms")

    if development.cover_image:
        main_image = development.cover_image
    elif images.exists():
        main_image = images.first()
    else:
        main_image = None

    main_image_alt = development.name

    if hasattr(main_image, "alt_text") and main_image.alt_text:
        main_image_alt = main_image.alt_text

    return render(
        request,
        "developments/development_detail.html",
        {
            "development": development,
            "images": images,
            "main_image": main_image,
            "main_image_alt": main_image_alt,
            "unit_types": unit_types,
        },
    )
