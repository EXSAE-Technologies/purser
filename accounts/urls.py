from rest_framework import routers
from django.urls import path
from .views import (
    UserViewSet,
    AccountLogin,
    AccountProfile,
    AccountMain
)
from django.contrib.auth.views import logout_then_login

router = routers.DefaultRouter()
router.register(r'user',UserViewSet,basename="user")

app_name="accounts"
urlpatterns = [
    path('login/',AccountLogin.as_view(),name="login"),
    path('logout/',logout_then_login,name="logout"),
    path('id/<pk>/',AccountProfile.as_view(),name="profile"),
    path('',AccountMain.as_view(),name="main"),
    path('profile/',AccountMain.as_view(),name="profile2")
]
