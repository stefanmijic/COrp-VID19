from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("countries", views.countries, name="countries"),
        path("states", views.states, name="states"),
        path("cities", views.cities, name="cities"),
        path("universities", views.universities, name="universities"),
        path("corporations", views.corporations, name="corporations"),
    ]
