from rest_framework import routers
from django.urls import path
from .views import (
    UserViewSet,
    AccountLogin
)

router = routers.DefaultRouter()
router.register(r'user',UserViewSet,basename="user")

app_name="accounts"
urlpatterns = [
    path('login/',AccountLogin.as_view(),name="login"),
]
