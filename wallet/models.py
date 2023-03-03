from django.db import models
import uuid
from django.contrib.auth.models import User

class Wallet(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False)
    user=models.ForeignKey(User,related_name="wallets",on_delete=models.CASCADE)
    CURRENCY=(
        ("zmw","ZMW"),
    )
    currency=models.CharField(max_length=200,choices=CURRENCY)
    balance=models.FloatField(default=0.0,editable=False)
    active=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return str(self.id)

class FlutterwavePayment(models.Model):
    id=models.BigIntegerField(primary_key=True,unique=True)
    tx_ref=models.CharField(max_length=200)
    amount=models.FloatField()
    charged_amount=models.FloatField()
    currency=models.CharField(max_length=200)
    app_fee=models.FloatField()
    merchant_fee=models.FloatField()
    processor_response=models.TextField()
    narration=models.TextField()
    status=models.CharField(max_length=200)
    payment_type=models.CharField(max_length=200)
    created_at=models.DateTimeField()
    
    def __str__(self) -> str:
        return self.tx_ref
    
class FlutterwaveTransfer(models.Model):
    id=models.BigIntegerField(primary_key=True,unique=True)
    account_number=models.CharField(max_length=200)
    bank_name=models.CharField(max_length=200)
    bank_code=models.CharField(max_length=200)
    fullname=models.CharField(max_length=200)
    currency=models.CharField(max_length=200)
    debit_currency=models.CharField(max_length=200)
    amount=models.FloatField()
    fee=models.FloatField()
    status=models.CharField(max_length=200)
    reference=models.CharField(max_length=200)
    narration=models.TextField()
    is_approved=models.BooleanField()
    created_at=models.DateTimeField()
    
    def __str__(self) -> str:
        return self.reference

class Transaction(models.Model):
    tx_ref=models.CharField(max_length=200, unique=True)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    amount=models.FloatField()
    approved=models.BooleanField(default=False,editable=False)
    
    def __str__(self) -> str:
        return "txn-"+str(self.id)