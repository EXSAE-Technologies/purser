from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Wallet,
    Transaction
)
from .serializers import (
    WalletSerializer,
    TransactionSerializer
)
from rest_framework.permissions import AllowAny

class WalletViewSet(ModelViewSet):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer
    permission_classes=[AllowAny]
    
    @action(detail=True,methods=['post'])
    def send(self,request,pk):
        return Response(request.POST)

class TransactionViewSet(ReadOnlyModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
    permission_classes=[AllowAny]
