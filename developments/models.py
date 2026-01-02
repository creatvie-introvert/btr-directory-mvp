from django.db import models
from cities.models import City


# Create your models here.
class Development(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="developments")

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    area_name = models.CharField(max_length=120, blank=True)

    cover_image = models.ImageField(upload_to="developments/", blank=True)
    cover_image_alt = models.CharField(
        max_length=120,
        blank=True,
        help_text="Describe the image for screen readers."
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
