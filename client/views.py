from django.shortcuts import render
from .models import FidClient
from .ClientSerializer import ClientSerializer
from rest_framework import viewsets

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = FidClient.objects.all()