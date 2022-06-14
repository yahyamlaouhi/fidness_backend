from rest_framework import serializers
from .models import FidPdv,FidKeyWordsMarque,FidPlaces




class FidPdvSerializer(serializers.ModelSerializer):

    class Meta:
        model = FidPdv
        fields = ['id_marque','adresse','latitude','longitude']


class FidKeyWordsMarqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = FidKeyWordsMarque
        fields = ['key_word','fid_marque']

class FidPlaces(serializers.ModelSerializer):

    class Meta:
        model = FidPlaces
        fields = ['visited_places','latitude','longitude','fid_marque']




class distanceSerializer(serializers.Serializer):
    destinationA_lat = serializers.FloatField()
    destinationA_lon = serializers.FloatField()
    destinationB_lat = serializers.FloatField()
    destinationB_lon = serializers.FloatField()

    



