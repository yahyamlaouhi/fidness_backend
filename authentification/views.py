from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from .models import AuthUser
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import viewsets
from django.core import serializers
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm

from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import generics


def home(request):
    return render(request, 'users/home.html')


# class RegisterView(View):
#     form_class = RegisterForm
#     initial = {'key': 'value'}
#     # template_name = 'users/register.html'

#     def dispatch(self, request, *args, **kwargs):
#         # will redirect to the home page if a user tries to access the register page while logged in
#         if request.user.is_authenticated:
#             return redirect(to='/')

#         # else process dispatch as it otherwise normally would
#         return super(RegisterView, self).dispatch(request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return Response(request, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             form.save()

#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}')

#             return redirect(to='login')

#         return Response(request, {'form': form})


# # Class based view that extends from the built in login view to add a remember me functionality
# class CustomLoginView(LoginView):
#     form_class = LoginForm

#     def form_valid(self, form):
#         remember_me = form.cleaned_data.get('remember_me')

#         if not remember_me:
#             # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
#             self.request.session.set_expiry(0)

#             # Set session as modified to force data updates/cookie to be saved.
#             self.request.session.modified = True

#         # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
#         return super(CustomLoginView, self).form_valid(form)


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer



# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='users-profile')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)

#     return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})


def home(request):
    return render(request, 'users/home.html')


@api_view(['GET', 'POST'])
def getuser(request):
    if request.method == 'GET':
        User = get_user_model()
        users = User.objects.all()
        tmpJson = serializers.serialize("json",users)
        return Response(tmpJson) 

class UserViewSet(viewsets.ModelViewSet):
    serializer_class =UserSerializer
    queryset = AuthUser.objects.all()