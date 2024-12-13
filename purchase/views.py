from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import PurchaseService
from .models import MyUser

purchase_service = PurchaseService()


class BuyCryptoView(APIView):
    def post(self, request):
        coin_name = request.data.get('coin_name')
        quantity = request.data.get('quantity')
        user_id = request.data.get('user_id')

        try:
            user = MyUser.objects.get(id=user_id)
            purchase_service.handle_purchase(user, coin_name, quantity)

            return Response({'message': 'Purchase successful', 'user_balance': user.balance},
                            status=status.HTTP_200_OK)
        except MyUser.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

