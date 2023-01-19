"""purser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from wallet.urls import router as wallet_router
from accounts.urls import router as accounts_router

main_router = DefaultRouter()

main_router.registry.extend(wallet_router.registry)
main_router.registry.extend(accounts_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(main_router.urls)),
    path('openapi/',get_schema_view(
        title="Purser",
        description="eWallet API",
        version="1.0.0"
    ),name="openapi-schema"),
    path('redoc/', TemplateView.as_view(
        template_name='api/redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
]
