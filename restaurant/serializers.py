from rest_framework import serializers
from decimal import Decimal
from .models import Booking, Menu


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','Name','No_of_guests','BookingDate']
        extra_kwargs = {
            'No_of_guests':{'min_value':1}
        }

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','Title','Price','Inventory']
        extra_kwargs = {
            'Inventory':{'min_value':0}
        }