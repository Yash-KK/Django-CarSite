from django.shortcuts import get_object_or_404, render

from .models import (
    Car
)

# Create your views here.
def car_detail(request,id):
    car = get_object_or_404(Car,pk=id)
    data = {
        'car':car
    }
    return render(request,'Car/car_detail.html',data)

def cars(request):
    allcars = Car.objects.order_by('-created_date')
    data = {
        'cars':allcars
    }
    return render(request,'Car/cars.html',data)

def search(request):
    cars = Car.objects.order_by('-created_date')
    year_search = Car.objects.all().values_list('year',flat=True).distinct()
    model_search = Car.objects.all().values_list('model',flat=True).distinct()
    body_style_search = Car.objects.all().values_list('body_style',flat=True).distinct()
    city_search = Car.objects.all().values_list('city',flat=True).distinct()
    transmission_search = Car.objects.all().values_list('transmission',flat=True).distinct()
    
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        cars = cars.filter(description__icontains = keyword)
    
    if 'model' in request.GET:
        model = request.GET['model']
        cars = cars.filter(model__iexact=model)    
    
    if 'state' in request.GET:
        state = request.GET['state']
        cars = cars.filter(state__iexact=state)     
    
    if 'year' in request.GET:
        year = request.GET['year']
        cars = cars.filter(year__iexact=year)  
    
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)  
    
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if min_price !=0:        
            cars = cars.filter(price__gte=min_price, price__lte=max_price)
               
           
    
    data = {
        'cars':cars,
        'year_search':year_search,        
        'model_search':model_search,        
        'body_style_search':body_style_search,
        'city_search': city_search,
        'transmission_search':transmission_search        
        
    }
    return render(request,'Car/search.html',data)
