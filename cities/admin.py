from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import City


# Register your models here.
@admin.register(City)
class CityAdmin(SummernoteModelAdmin):
    """
    Admin configuration for City.
    """

    list_display = (
        "name", "is_active", "created_at", "updated_at", "show_on_homepage"
    )
    list_filter = ("is_active",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)
    summernote_fields = ("description")
