from django.contrib import admin 
from django.urls import path 
from . import views
from restaurant.views import sayHello 
  
urlpatterns = [ 
    #path('', sayHello, name='sayHello'),
    path('', views.index, name='index')
]