from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class PurchaseRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin_name = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    dollar_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)