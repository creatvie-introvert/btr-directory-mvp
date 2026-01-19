"""
URL routes for the core app.
"""
from django.urls import path
from . import views

app_name = "core"


urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("what_is_btr/", views.what_is_btr, name="what_is_btr"),
    path("about/", views.about, name="about")
]
