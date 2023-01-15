from rest_framework.routers import DefaultRouter
from .views import (
    WalletViewSet,
    TransactionViewSet,
    SendMoneyViewSet,
    FlutterwaveWebhook
)
router = DefaultRouter()

router.register(r"wallet",viewset=WalletViewSet)
router.register(r"transaction",viewset=TransactionViewSet)
router.register(r"send-money",viewset=SendMoneyViewSet,basename="send-money")
router.register(r"flutterwave-webhook",viewset=FlutterwaveWebhook,basename="flutterwave")

app_name="wallet"
urlpatterns = router.urls
