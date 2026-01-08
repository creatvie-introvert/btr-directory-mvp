from django.db import models
from cities.models import City


# Create your models here.
class Development(models.Model):
    class TenancyOption(models.TextChoices):
        LONG_TERM = "long-term", "Long-term"
        FLEXIBLE = "flexible", "Flexible"
        SHORT_STAY_AVAILABLE = "short-stay-available", "Short-stay available"

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="developments")

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    area_name = models.CharField(max_length=120, blank=True)

    address_line = models.CharField(max_length=225, blank=True)
    postcode = models.CharField(max_length=20, blank=True)

    summary = models.TextField(blank=True)
    description = models.TextField(blank=True)

    tenancy_options = models.CharField(
        max_length=30,
        choices=TenancyOption.choices,
        blank=True,
    )
    website_url = models.URLField(blank=True)

    operator_name = models.CharField(max_length=120, blank=True)
    operator_contact_email = models.EmailField(blank=True)

    cover_image = models.ImageField(upload_to="developments/", blank=True)
    cover_image_alt = models.CharField(
        max_length=120,
        blank=True,
        help_text="Describe the image for screen readers.",
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["city"]),
            models.Index(fields=["is_active"]),
        ]

    def __str__(self) -> str:
        return self.name


class DevelopmentImage(models.Model):
    development = models.ForeignKey(
        Development, on_delete=models.CASCADE, related_name="images"
    )

    image = models.ImageField(upload_to="developments/")
    alt_text = models.CharField(
        max_length=120,
        blank=True,
        help_text="Describe the image for screen readers.",
    )

    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "id"]
    
    def __str__(self) -> str:
        return f"{self.development.name} image {self.id}"
