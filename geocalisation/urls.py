from . import views
from django.urls import path

urlpatterns = [
    path('distance/', views.distance),
    path('similarity/', views.geolocalisation_api),


]