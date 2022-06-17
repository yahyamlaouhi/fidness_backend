from django.shortcuts import render
from .models import FidAdmin
from .superadminSerializer import SuperAdminSerializer
from rest_framework import viewsets

# Create your views here.
class SuperAdminViewSet(viewsets.ModelViewSet):
    serializer_class = SuperAdminSerializer
    queryset = FidAdmin.objects.all()