from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Wallet,
    Transaction
)
from .serializers import (
    WalletSerializer,
    TransactionSerializer,
    SendMoneySerializer,
    FlutterwavePaymentSerializer
)
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.schemas import ManualSchema
import coreapi

class WalletViewSet(ModelViewSet):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer
    permission_classes=[AllowAny]

class TransactionViewSet(ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
    permission_classes=[AllowAny]

class SendMoneyViewSet(ViewSet):
    create_schema=ManualSchema(fields=[
        coreapi.Field("from_wallet",True,"form")
    ])
    def create(self,request,schema=create_schema):
        send_money = SendMoneySerializer(data=request.data)
        if send_money.is_valid():
            send_money.save()
            return Response(send_money.data)
        return Response(send_money.errors,status=status.HTTP_400_BAD_REQUEST)

class FlutterwaveWebhook(ViewSet):
    def create(self,request,*args,**kwargs):
        if request.data["event"] == "charge.completed":
            fltxn = FlutterwavePaymentSerializer(data=request.data["data"])
            if fltxn.is_valid():
                fltxn.save()
                txn = Transaction.objects.get(tx_ref=fltxn.data["tx_ref"])
                if fltxn.data["status"] == "successful":
                    txn.approved = True
                    txn.save()
                return Response(TransactionSerializer(txn).data)
            return Response(txn.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({},status=status.HTTP_400_BAD_REQUEST)
