from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Menu, Booking
from rest_framework import viewsets
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'Restaurant App'})


class MenuItemView(generics.ListCreateAPIView):
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   permission_classes = [permissions.IsAuthenticated] 