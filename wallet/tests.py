from django.test import TestCase
from rest_framework.test import APITestCase
from rich import print
from django.contrib.auth.models import User

successfull_payment_data = {
  "event": "charge.completed",
  "data": {
    "id": 285959875,
    "tx_ref": "Links-616626414629",
    "flw_ref": "PeterEkene/FLW270177170",
    "device_fingerprint": "a42937f4a73ce8bb8b8df14e63a2df31",
    "amount": 100,
    "currency": "NGN",
    "charged_amount": 100,
    "app_fee": 1.4,
    "merchant_fee": 0,
    "processor_response": "Approved by Financial Institution",
    "auth_model": "PIN",
    "ip": "197.210.64.96",
    "narration": "CARD Transaction ",
    "status": "successful",
    "payment_type": "card",
    "created_at": "2020-07-06T19:17:04.000Z",
    "account_id": 17321,
    "customer": {
      "id": 215604089,
      "name": "Yemi Desola",
      "phone_number": None,
      "email": "user@gmail.com",
      "created_at": "2020-07-06T19:17:04.000Z"
    },
    "card": {
      "first_6digits": "123456",
      "last_4digits": "7889",
      "issuer": "VERVE FIRST CITY MONUMENT BANK PLC",
      "country": "NG",
      "type": "VERVE",
      "expiry": "02/23"
    }
  }
}

# Create your tests here.
class WalletAPITests(APITestCase):
    def setUp(self) -> None:
        User.objects.create_user("fshangala","fshangala@gmail.com","8224646fundu")
        
    def test_create_wallet(self):
        response = self.client.post("/wallet/",{
            "currency":"zmw",
            "user":1
        })
        print(response.json())
        self.assertTrue("id" in response.json())
        
    def test_flutterwave_webhook(self):
        response = self.client.post("/wallet/",{
            "currency":"zmw",
            "user":1
        })
        wallet = response.json()
        print(wallet)
        self.assertTrue("id" in wallet)
        
        response = self.client.post("/transaction/",{
            "tx_ref":"Links-616626414629",
            "amount": 100,
            "wallet":wallet["id"]
        })
        transaction = response.json()
        print(transaction)
        self.assertTrue("id" in transaction)
        
        response = self.client.post('/flutterwave-webhook/', successfull_payment_data,"json")
        print(response.json())