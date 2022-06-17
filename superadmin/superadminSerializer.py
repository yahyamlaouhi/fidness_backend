from rest_framework import serializers 
from superadmin.models import FidAdmin
 
 
class SuperAdminSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FidAdmin
        fields = '__all__'