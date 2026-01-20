"""
URL routes for the core app.
"""
from django.urls import path
from . import views

app_name = "core"


urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("what-is-btr/", views.what_is_btr, name="what_is_btr"),
    path("about/", views.about, name="about"),
    path("disclaimer/", views.disclaimer, name="disclaimer"),
    path(
        "accessibility-statement/",
        views.accessibility_statement,
        name="accessibility_statement",
    ),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("terms-of-use/", views.terms_of_use, name="terms_of_use"),
]
