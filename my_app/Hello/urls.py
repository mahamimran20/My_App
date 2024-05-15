from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("Maham", views.Maham, name="Maham"),
    path("Imran", views.Imran, name="Imran")
]