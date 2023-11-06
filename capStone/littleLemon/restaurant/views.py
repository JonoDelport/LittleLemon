from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu
from .models import Booking
from .serializers import MenuItemSerializer
from .serializers import BookingSerializer

# Create your views here.

def sayHello(request):
    return HttpResponse("Hello World")

def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()  # Provide the queryset of MenuItem objects
    serializer_class = MenuItemSerializer # Use the MenuItemSerializer for serialization

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  # Provide the queryset of MenuItem objects
    serializer_class = MenuItemSerializer # Use the MenuItemSerializer for serialization

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer