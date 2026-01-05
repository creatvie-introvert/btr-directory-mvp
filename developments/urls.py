from django.urls import path
from . import views

app_name = "developments"

urlpatterns = [
    path("<slug:slug>/", views.development_detail, name="detail"),
]
