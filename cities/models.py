"""
Database models for cities.

A City is used to group developments and support city-based browsing.
"""

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to="cities/", blank=True)
    image_alt = models.CharField(
        max_length=120,
        blank=True,
        help_text="Describe the image for screen readers.",
    )

    is_active = models.BooleanField(default=True)
    show_on_homepage = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["is_active"]),
            models.Index(fields=["show_on_homepage"]),
        ]

    def __str__(self) -> str:
        return self.name
