from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'partner', views.PartnerViewSet, basename='partenaire')
router.register(r'superadmin', views.SuperAdminViewSet, basename='admin')
router.register(r'client', views.ClientViewSet, basename='customer')
router.register(r'pays', views.PaysViewSet, basename='pays')

urlpatterns = [
    path('',include(router.urls)),
    path('prediction/<int:pk>/', views.prediction),
]