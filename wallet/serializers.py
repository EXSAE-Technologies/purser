from rest_framework import serializers
from .models import (
    Wallet,
    Transaction,
    FlutterwavePayment
)

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields="__all__"

class FlutterwavePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlutterwavePayment
        fields="__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields="__all__"

class SendMoneySerializer(serializers.Serializer):
    from_wallet=serializers.UUIDField()
    to_wallet=serializers.UUIDField()
    amount=serializers.FloatField()
    
    def create(self, validated_data):
            Transaction.objects.create(
                wallet=validated_data["from_wallet"],
                amount=validated_data["amount"]*(-1)
            )
            Transaction.objects.create(
                wallet=validated_data["to_wallet"],
                amount=validated_data["amount"]
            )
