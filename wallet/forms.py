from django import forms
from .models import (
  Transaction,
  Wallet
)
import uuid

class TransactionForm(forms.Form):
  antecedent=forms.IntegerField()
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
  