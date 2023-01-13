from rest_framework.routers import DefaultRouter
from .views import (
    WalletViewSet,
    TransactionViewSet
)

router = DefaultRouter()
router.register(r"wallet",viewset=WalletViewSet)
router.register(r"transaction",viewset=TransactionViewSet)

app_name="wallet"
urlpatterns = router.urls
