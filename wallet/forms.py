from django import forms
from .models import (
  Transaction,
  Wallet
)
import uuid

class TransactionForm(forms.Form):
  #antecedent=forms.IntegerField()
  tx_ref=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Reference'
  }))
  from_wallet=forms.ModelChoiceField(Wallet.objects.all(),required=True,widget=forms.Select(attrs={
    'class':'form-control',
  }))
  amount=forms.FloatField(required=True,widget=forms.NumberInput(attrs={
    'class':'form-control',
    'step':'0.5',
    'placeholder':'Amount'
  }))
  to_wallet=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={
    'class':'form-control',
    'placeholder':'To Wallet ID'
  }))
  
  def __init__(self,*args,**kwargs):
    self.request = kwargs.pop("request")
    super(forms.Form, self).__init__(*args,**kwargs)
    self.fields['from_wallet'].queryset=self.get_queryset()
    self.fields['tx_ref'].initial = uuid.uuid4()
  
  def get_queryset(self):
    return self.request.user.wallets.all()
  
  def save(self):
    #antecendent = Transaction.objects.get(pk=self.cleaned_data["antecedent"])
    from_wallet = self.cleaned_data["from_wallet"]
    to_wallet = Wallet.objects.get(pk=self.cleaned_data["to_wallet"])
    
    antecedent = Transaction.objects.create(
      tx_ref=self.cleaned_data["tx_ref"],
      wallet=from_wallet,
      amount=-1*float(self.cleaned_data["amount"])
    )
    
    Transaction.objects.create(
      antecedent=antecedent.id,
      wallet=to_wallet,
      amount=float(self.cleaned_data["amount"])
    )
    
  
  def is_valid(self):
    try:
      to_wallet = Wallet.objects.get(pk=self.data.get("to_wallet"))
    except Wallet.DoesNotExist as e:
      print(e)
      return False
    else:
      return super().is_valid()
  