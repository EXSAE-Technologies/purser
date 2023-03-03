from rest_framework.routers import DefaultRouter
from .views import (
    WalletViewSet,
    TransactionViewSet,
    SendMoneyViewSet,
    FlutterwaveWebhook
)
from django.urls import path
from .views import (
    WalletList
)
router = DefaultRouter()

router.register(r"wallet",viewset=WalletViewSet)
router.register(r"transaction",viewset=TransactionViewSet)
router.register(r"send-money",viewset=SendMoneyViewSet,basename="send-money")
router.register(r"flutterwave-webhook",viewset=FlutterwaveWebhook,basename="flutterwave")

app_name="wallet"
urlpatterns = [
    path('',WalletList.as_view(), name="list"),
]
