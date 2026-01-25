from django import forms

from cities.models import City


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
