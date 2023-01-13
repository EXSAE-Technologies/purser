from django.db import models
import uuid
from django.contrib.auth.models import User

class Wallet(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    CURRENCY=(
        ("zmw","ZMW"),
    )
    currency=models.CharField(max_length=200,choices=CURRENCY)
    balance=models.FloatField(default=0.0,editable=False)
    active=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return str(self.id)

class Transaction(models.Model):
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    amount=models.FloatField()
    approved=models.BooleanField(default=False,editable=False)
    
    def __str__(self) -> str:
        return "txn-"+str(self.id)