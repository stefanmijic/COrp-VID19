from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("countries", views.countries, name="countries"),
        path("country/<country>", views.country_detail, name="country_detail"),
        path("states", views.states, name="states"),
        path("cities", views.cities, name="cities"),
        path("universities", views.universities, name="universities"),
        path("university/<aid>", views.university_detail, name="university_detail"),
        path("corporations", views.corporations, name="corporations"),
        path("measure/<mid>", views.measure_detail, name="measure_detail"),
    ]
