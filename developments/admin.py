from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Development, DevelopmentImage


# Register your models here.
class DevelopmentImageInline(admin.TabularInline):
    model = DevelopmentImage
    extra = 1


@admin.register(Development)
class DevelopmentAdmin(SummernoteModelAdmin):
    list_display = ("name", "city", "area_name", "is_active", "updated_at")
    list_filter = ("city", "is_active")
    search_fields = ("name", "area_name")
    prepopulated_fields = {"slug": ("name",)}
    summernote_fields = ("description")
    inlines = [DevelopmentImageInline]


@admin.register(DevelopmentImage)
class DevelopmentImageAdmin(admin.ModelAdmin):
    list_display = ("development", "sort_order", "id")
    list_filter = ("development",)
