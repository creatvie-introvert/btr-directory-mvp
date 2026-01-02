from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to="cities/", blank=True)
    image_alt = models.CharField(max_length=120, blank=True, help_text="Describe the image for screen readers.")

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    show_on_homepage = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=["is_active"]),
            models.Index(fields=["show_on_homepage"]),
        ]
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
