
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import MyTokenObtainPairView,RegisterView, getuser
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'user', views.UserViewSet, basename='partenaire')
urlpatterns = [
    path('', views.getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',include(router.urls)),   
    path('register/', RegisterView.as_view(), name='auth_register'),






]
