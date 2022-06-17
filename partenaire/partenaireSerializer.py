from rest_framework import serializers 
from partenaire.models import FidCarteFidelite
 
 
class PartnerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FidCarteFidelite
        fields = '__all__'