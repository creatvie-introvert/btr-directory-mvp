from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Development, DevelopmentImage, Amenity, UnitType


# Register your models here.
class DevelopmentImageInline(admin.TabularInline):
    model = DevelopmentImage
    extra = 0


class UnitTypeInline(admin.TabularInline):
    model = UnitType
    extra = 0
    fields = ("bedrooms", "rent_from_pcm", "rent_to_pcm", "is_available")


@admin.register(Development)
class DevelopmentAdmin(SummernoteModelAdmin):
    list_display = (
        "name",
        "city",
        "area_name",
        "is_active",
        "property_type",
        "minimum_term_months",
        "updated_at"
    )
    list_filter = (
        "city",
        "is_active",
        "property_type",
        "tenancy_options"
    )
    search_fields = ("name", "area_name", "postcode", "operator_name")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")
    filter_horizontal = ("amenities",)
    fieldsets = (
        ("Core", {
            "fields": (
                "city",
                "name",
                "slug",
                "is_active",
            )
        }),
        ("Location", {
            "fields": (
                "area_name",
                "address_line",
                "postcode",
            )
        }),
        ("Overview", {
            "fields": (
                "summary",
                "description",
                "website_url",
            )
        }),
        ("Key facts", {
            "fields": (
                "property_type",
                "number_of_homes",
            )
        }),
        ("Amenities", {
            "fields": (
                "amenities",
            )
        }),
        ("Tenancy", {
            "fields": (
                "tenancy_options",
                "tenancy_length",
                "minimum_term_months",
                "furnishing",
                "pet_policy",
                "bills_included",
            )
        }),
        ("Operator", {
            "fields": (
                "operator_name",
                "operator_contact_email",
            )
        }),
        ("Media", {
            "fields": (
                "cover_image",
                "cover_image_alt",
            )
        }),
        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )
    summernote_fields = ("description",)
    inlines = [DevelopmentImageInline, UnitTypeInline]


@admin.register(DevelopmentImage)
class DevelopmentImageAdmin(admin.ModelAdmin):
    list_display = ("development", "sort_order", "id")
    list_filter = ("development",)
    readonly_fields = ("created_at",)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(UnitType)
class UnitTypeAdmin(admin.ModelAdmin):
    list_display = ("development", "bedrooms", "rent_from_pcm", "rent_to_pcm", "is_available", "updated_at")
    list_filter = ("is_available", "bedrooms", "development__city")
    search_fields = ("development__name", "development__city__name", "development__postcode")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("development", "bedrooms")
    autocomplete_fields = ("development",)

