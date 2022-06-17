from rest_framework import serializers 
from client.models import FidClient
 
 
class ClientSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FidClient
        fields = '__all__'