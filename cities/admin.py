from django.contrib import admin
from .models import City


# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """
    Admin configuration for City.
    """

    list_display = ("name", "is_active", "created_at", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)
