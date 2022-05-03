from django.http import HttpResponse
from django.shortcuts import render

from .models import (
    Team
)
from Car.models import (
    Car 
)

# Create your views here.

def home(request):
    team = Team.objects.order_by('created_at')
    cars = Car.objects.order_by('-created_date')
    
    year_search = Car.objects.all().values_list('year',flat=True).distinct()
    model_search = Car.objects.all().values_list('model',flat=True).distinct()
    state_search = Car.objects.all().values_list('state',flat=True).distinct()
    body_style_search = Car.objects.all().values_list('body_style',flat=True).distinct()
    data = {
        'team':team,
        'cars':cars,
        
        'year_search':year_search,
        'model_search':model_search,
        'state_search':state_search,
        'body_style_search':body_style_search,
    }
    return render(request,'Pages/home.html',data)


def about(request):
    team = Team.objects.order_by('created_at')
    data = {
        'team':team
    }
    return render(request,'Pages/about.html',data)

def contact(request):
    return render(request,'Pages/contact.html')

def services(request):
    return render(request,'Pages/services.html') 