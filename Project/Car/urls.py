from django.urls import path

from . import views

urlpatterns = [
    path("detail/<int:id>",views.car_detail,name='car-detail'),
    path("allcars/",views.cars,name='cars'),
    path("search/",views.search,name='search')
]
