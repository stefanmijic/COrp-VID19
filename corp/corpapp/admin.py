from django.contrib import admin
from .models import University, Corporation, State, Country, City, Measure, Implemented

admin.site.register(University)
admin.site.register(Corporation)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Measure)
admin.site.register(Implemented)
