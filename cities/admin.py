"""
Admin configuration for cities.

Controls how City records are displayed and managed in the admin dashboard.
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import City


@admin.register(City)
class CityAdmin(SummernoteModelAdmin):
    list_display = (
        "name",
        "is_active",
        "created_at",
        "updated_at",
        "show_on_homepage",
    )
    list_filter = ("is_active",)
    search_fields = ("name", "slug")
    ordering = ("name",)
    list_per_page = 50

    prepopulated_fields = {"slug": ("name",)}
    summernote_fields = ("description",)
