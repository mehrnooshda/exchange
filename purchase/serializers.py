from rest_framework import serializers
from .models import MyUser, PurchaseRequest

class PurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = ['user', 'coin_name', 'quantity', 'dollar_value']

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'balance']
