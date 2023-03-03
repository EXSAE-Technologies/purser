from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView, RedirectView, FormView
from django.conf import settings
from django.urls import reverse

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]

class AccountLogin(LoginView):
    template_name="registration/login.html"


class UserRegister(FormView):
    form_class=UserCreationForm
    success_url=settings.LOGIN_URL
    template_name="registration/register.html"
    
    def form_valid(self, form):
        user = User.objects.create(username=form.cleaned_data["username"])
        user.set_password(form.cleaned_data["password1"])
        user.save()
        return super().form_valid(form)
    
class AccountMain(RedirectView):
    pattern_name="accounts:profile"
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse(self.pattern_name, kwargs={"pk":self.request.user.id})

class AccountProfile(DetailView):
    model=User
    context_object_name="user"