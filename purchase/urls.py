from django.urls import path
from .views import BuyCryptoView

urlpatterns = [
    path('buy-crypto/', BuyCryptoView.as_view(), name='buy-crypto'),
]