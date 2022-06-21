from rest_framework import serializers
from .models import FidClient,FidCarteFidelite,FidAdmin, FidGouvernorat

class FidClientSerialiser(serializers.ModelSerializer):
    class Meta:
        model = FidClient
        fields = '__all__'
 
 
class PartnerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FidCarteFidelite
        fields = '__all__'


 
class SuperAdminSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FidAdmin
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FidClient
        fields = '__all__'


{"pays":"bizerte",
    "sexe" :"homme",
    "age" :25,
    "carte":"True",
    "tempon_numbers":6,
   "year_numbers":2022,
    "new_age":29,
    "new_age_score":23,
   "new_tempon_score":50}


class PaysSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FidGouvernorat
        fields = '__all__'


