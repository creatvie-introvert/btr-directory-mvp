from django import forms

from cities.models import City
from developments.models import Development


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = (
            "name",
            "slug",
            "description",
            "image",
            "image_alt",
            "is_active",
            "show_on_homepage",
        )


class DevelopmentForm(forms.ModelForm):
    class Meta:
        model = Development
        fields = (
            "city",
            "name",
            "slug",
            "area_name",
            "postcode",
            "description",
            "summary",
            "cover_image",
            "cover_image_alt",
            "is_active",
        )
