from rest_framework import serializers
from .models import FidPdv,FidGeolocalisation




class FidPdvSerializer(serializers.ModelSerializer):

    class Meta:
        model = FidPdv
        fields = ['id_marque','adresse','latitude','longitude']


class FidGeolocalisationSerializer(serializers.ModelSerializer):

    class Meta:
        model =FidGeolocalisation
        fields ='__all__'




class geolocationInformationSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()


    



