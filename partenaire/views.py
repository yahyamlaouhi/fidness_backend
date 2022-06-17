from django.shortcuts import render
from .models import FidCarteFidelite
from .partenaireSerializer import PartnerSerializer
from rest_framework import viewsets

# Create your views here.
class PartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    queryset = FidCarteFidelite.objects.all()