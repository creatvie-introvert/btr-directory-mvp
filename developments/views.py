from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import Development, DevelopmentImage, Enquiry


def development_detail(request, slug):
    """
    Shows one development page.

    Loads the development record, its images, and its unit types.
    Chooses a main image (cover image first, then first gallery image,
    otherwise none).
    """

    development = get_object_or_404(Development, slug=slug)

    images = (
        DevelopmentImage.objects
        .filter(development=development)
        .order_by("sort_order", "id")
    )

    unit_types = development.unit_types.order_by("bedrooms")

    # Choose the main image(cover > first image > none)
    if development.cover_image:
        main_image = development.cover_image
    elif images.exists():
        main_image = images.first()
    else:
        main_image = None

    main_image_alt = development.name

    # If we have a main image, and it has an alt_text value, use it
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


def enquiry_create(request, slug):
    """
    Shows + submits the enquiry form page for one development.

    GET -> show blank form
    POST -> validate, seve Enquiry, redirect (prevents double submit on
    refresh)
    """

    development = get_object_or_404(Development, slug=slug, is_active=True)

    # For showing a simple "sent message after redirect"
    sent = request.GET.get("sent") == "1"

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        errors = {}

        if not full_name:
            errors["full_name"] = "Please enter your name."
        if not email:
            errors["email"] = "Please enter your email."
        else:
            # Email format validation
            try:
                validate_email(email)
            except ValidationError:
                errors["email"] = "Please enter a valid email address."
        if not message:
            errors["message"] = "Please enter a message."

        if errors:
            # Re-render the page with the user's input + errors
            return render(
                request,
                "developments/enquiry_form.html",
                {
                    "development": development,
                    "errors": errors,
                    "form_data": {
                        "full_name": full_name,
                        "email": email,
                        "message": message,
                    },
                    "sent": False,
                },
            )
        Enquiry.objects.create(
            development=development,
            full_name=full_name,
            email=email,
            message=message,
        )

        return redirect(f"{reverse('developments:enquire', kwargs={'slug': development.slug})}?sent=1")

    return render(
        request,
        "developments/enquiry_form.html",
        {
            "development": development,
            "sent": sent,
            "errors": {},
            "form_data": {},
        },
    )
