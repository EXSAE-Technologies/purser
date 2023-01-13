from rest_framework import serializers
from .models import (
    Wallet,
    Transaction
)

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields="__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields="__all__"
