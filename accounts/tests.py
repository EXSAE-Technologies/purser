from rest_framework.test import APITestCase
from rich import print

# Create your tests here.
class AccountTests(APITestCase):
    def test_create_user(self):
        response = self.client.post('/user/',{
            'username':"fshangala",
            "password":"8224646fundu",
            'email':"fshangala@gmail.com"
        })
        print(response.json())