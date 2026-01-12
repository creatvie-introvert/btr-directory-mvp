"""
Admin configuratio for managing developments, images, amenities, and unit
types.
"""

from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import (
    Development,
    DevelopmentImage,
    Amenity,
    UnitType
)


# Inlines shown inside the Development admin form
class DevelopmentImageInline(admin.TabularInline):
    model = DevelopmentImage
    extra = 0


class UnitTypeInline(admin.TabularInline):
    model = UnitType
    extra = 0
    fields = ("bedrooms", "rent_from_pcm", "rent_to_pcm", "is_available",)
    ordering = ("bedrooms",)


@admin.register(Development)
class DevelopmentAdmin(SummernoteModelAdmin):
    list_display = (
        "name",
        "city",
        "area_name",
        "is_active",
        "property_type",
        "minimum_term_months",
        "updated_at",
    )
    list_filter = (
        "city",
        "is_active",
        "property_type",
        "tenancy_options",
    )
    search_fields = ("name", "area_name", "postcode", "operator_name",)
    readonly_fields = ("created_at", "updated_at",)
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("amenities",)

    # Group field into sections to match the public detail page layout
    fieldsets = (
        ("Core", {
            "fields": (
                "city",
                "name",
                "slug",
                "is_active",
            ),
        }),
        ("Location", {
            "fields": (
                "area_name",
                "address_line",
                "postcode",
            ),
        }),
        ("Overview", {
            "fields": (
                "description",
                "summary",
                "website_url",
            ),
        }),
        ("Key facts", {
            "fields": (
                "rent_from_pcm",
                "deposit_from",
                "property_type",
                "number_of_homes",
                "pricing_note",
            ),
        }),
        ("Operator", {
            "fields": (
                "operator_name",
                "operator_contact_email",
            ),
        }),
        ("Amenities", {
            "fields": (
                "amenities",
            ),
        }),
        ("Tenancy", {
            "fields": (
                "tenancy_options",
                "tenancy_length",
                "minimum_term_months",
                "furnishing",
                "pet_policy",
                "bills_included",
            ),
        }),
        ("Media", {
            "fields": (
                "cover_image",
                "cover_image_alt",
            ),
        }),
        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            ),
        }),
    )

    inlines = [DevelopmentImageInline, UnitTypeInline]
    summernote_fields = ("description",)
    list_per_page = 25


@admin.register(DevelopmentImage)
class DevelopmentImageAdmin(admin.ModelAdmin):
    list_display = ("development", "sort_order", "id",)
    list_filter = ("development",)
    ordering = ("development", "sort_order", "id",)
    readonly_fields = ("created_at",)
    list_per_page = 100


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "updated_at",)
    list_filter = ("is_active",)
    search_fields = ("name", "development__name")
    readonly_fields = ("created_at", "updated_at",)
    list_per_page = 50


@admin.register(UnitType)
class UnitTypeAdmin(admin.ModelAdmin):
    list_display = (
        "development",
        "bedrooms",
        "rent_from_pcm",
        "rent_to_pcm",
        "is_available",
        "updated_at",
    )
    list_filter = ("is_available", "bedrooms", "development__city",)
    search_fields = (
        "development__name",
        "development__city__name",
        "development__postcode",
    )
    ordering = ("development", "bedrooms",)
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("development",)
