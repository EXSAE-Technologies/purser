from django.contrib import admin
from .models import (
    Wallet,
    Transaction
)

# Register your models here.
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display=["id","user","currency","balance","active"]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=["id","wallet","amount","approved"]