
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import MyTokenObtainPairView,RegisterView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),





]
