from rest_framework.test import APITestCase
from rest_framework import status
from .models import MyUser
from decimal import Decimal

class BuyCryptoViewTest(APITestCase):
    def setUp(self):
        self.user = MyUser.objects.create(username="Milooch", balance=50)

    def test_successful_purchase(self):
        response = self.client.post('/buy-crypto/', {
            'user_id': self.user.id,
            'coin_name': 'ETH',
            'quantity': '2'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Purchase successful')
        self.user.refresh_from_db()
        self.assertEqual(self.user.balance, Decimal('42'))  # 50 - (2 * 4)

    def test_user_not_found(self):
        response = self.client.post('/buy-crypto/', {
            'user_id': 10,
            'coin_name': 'ETH',
            'quantity': '2'
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'User does not exist')

    def test_unsupported_coin(self):
        response = self.client.post('/buy-crypto/', {
            'user_id': self.user.id,
            'coin_name': 'PEPE',
            'quantity': '2'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], "Coin 'PEPE' is not available. Please choose from: BTC, ETH, XRP, ADA, LTC")

    def test_insufficient_balance(self):
        response = self.client.post('/buy-crypto/', {
            'user_id': self.user.id,
            'coin_name': 'BTC',
            'quantity': '15'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], "Insufficient balance to complete this transaction.")

