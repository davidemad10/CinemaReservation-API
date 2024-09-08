from rest_framework import serializers
from .models import Guest,Movie,Reservation

class MovieSerializer(serializers.Modelserializer):
    class Meta:
        model=Movie
        fields='__all__'

class ReservationSerializer(serializers.Modelserializer):
    class Meta:
        model=Reservation
        fields='__all__'

class GuestSerializer(serializers.Modelserializer):
    class Meta:
        model=Guest
        fields=['pk','reservation','name','mobile']

