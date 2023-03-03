from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, RedirectView
from django.urls import reverse

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]

class AccountLogin(LoginView):
    template_name="registration/login.html"
    
class AccountMain(RedirectView):
    pattern_name="accounts:profile"
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse(self.pattern_name, kwargs={"pk":self.request.user.id})

class AccountProfile(DetailView):
    model=User