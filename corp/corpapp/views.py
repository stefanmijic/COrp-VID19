from django.shortcuts import render
from .models import University
from django.db.models.functions import Lower

def index(request):
    unilist = University.objects.order_by(Lower('name'))
    context = {'unilist': unilist}
    return render(request, 'corpapp/index.html', context)
