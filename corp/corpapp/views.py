from django.shortcuts import render
from .models import Country, State, City, University, Corporation
from django.db.models.functions import Lower

def index(request):
    return render(request, 'corpapp/index.html')

def countries(request):
    cntlist = Country.objects.order_by(Lower('name'))
    context = {'cntlist': cntlist}
    return render(request, 'corpapp/countries.html', context)

def country_detail(request, country):
    context = {'country': country}
    return render(request, 'corpapp/country_detail.html', context)

def states(request):
    stlist = State.objects.order_by(Lower('name'))
    context = {'stlist': stlist}
    return render(request, 'corpapp/states.html', context)

def cities(request):
    ctylist = City.objects.order_by(Lower('name'))
    context = {'ctylist': ctylist}
    return render(request, 'corpapp/cities.html', context)

def universities(request):
    unilist = University.objects.order_by(Lower('name'))
    context = {'unilist': unilist}
    return render(request, 'corpapp/universities.html', context)

def university_detail(request, aid):
    context = {'uni': University.objects.get(id=aid)}
    return render(request, 'corpapp/university_detail.html', context)

def corporations(request):
    corplist = Corporation.objects.order_by(Lower('name'))
    context = {'corplist': corplist}
    return render(request, 'corpapp/corporations.html', context)
