from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Development


# Register your models here.
@admin.register(Development)
class DevelopmentAdmin(SummernoteModelAdmin):
    list_display = ("name", "city", "area_name", "is_active", "updated_at")
    list_filter = ("city", "is_active")
    search_fields = ("name", "area_name")
    prepopulated_fields = {"slug": ("name",)}
    summernote_fields = ("description")
