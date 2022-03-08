from .models import GeoData
from rest_framework import serializers

class GeoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoData
        fields = ['name','longitude','latitude','geolocation']