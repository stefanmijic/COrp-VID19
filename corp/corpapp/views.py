from django.shortcuts import render
from .models import Country, State, City, University, Corporation, Measure, Implemented
from django.db.models.functions import Lower

def index(request):
    return render(request, 'corpapp/index.html', {'active_index': '0'})

def countries(request):
    cntlist = Country.objects.order_by(Lower('name'))
    context = {'cntlist': cntlist, 'active_index': '1'}
    return render(request, 'corpapp/countries.html', context)

def country_detail(request, country):
    context = {'country': country}
    return render(request, 'corpapp/country_detail.html', context)

def states(request):
    stlist = State.objects.order_by(Lower('name'))
    context = {'stlist': stlist, 'active_index': '2'}
    return render(request, 'corpapp/states.html', context)

def cities(request):
    ctylist = City.objects.order_by(Lower('name'))
    context = {'ctylist': ctylist}
    return render(request, 'corpapp/cities.html', context)

def universities(request):
    unilist = University.objects.order_by(Lower('name'))
    context = {'unilist': unilist, 'active_index': '4'}
    return render(request, 'corpapp/universities.html', context)

def university_detail(request, aid):
    implements = Implemented.objects.filter(entity_type=0, entity_id=aid).order_by('date')
    context = {'uni': University.objects.get(id=aid), 'impl': implements}
    return render(request, 'corpapp/university_detail.html', context)

def corporations(request):
    corplist = Corporation.objects.order_by(Lower('name'))
    context = {'corplist': corplist, 'active_index': '5'}
    return render(request, 'corpapp/corporations.html', context)

def measures(request):
    mlist = Measure.objects.order_by(Lower('name'))
    context = {'mlist': mlist, 'active_index': '3'}
    return render(request, 'corpapp/measures.html', context)

def measure_detail(request, mid):
    unis = Implemented.objects.filter(entity_type=0, measure=mid).order_by('date')
    uni_adoption_percent = len(unis) / len(University.objects.all()) * 100;
    context = {'measure': Measure.objects.get(id=mid), 'unis': unis, 'uni_adoption_percent': uni_adoption_percent}
    return render(request, 'corpapp/measure_detail.html', context)
