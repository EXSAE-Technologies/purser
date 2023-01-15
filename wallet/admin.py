from django.contrib import admin
from .models import (
    Wallet,
    Transaction,
    FlutterwavePayment
)

# Register your models here.
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display=["id","user","currency","balance","active"]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=["id","tx_ref","wallet","amount","approved"]

@admin.register(FlutterwavePayment)
class FlutterwavePaymentAdmin(admin.ModelAdmin):
    list_display=["id","tx_ref","amount","charged_amount","app_fee","merchant_fee","status"]