from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import json
from try2.models import Payment
from try2.serializers import PaymentSerializer

@api_view(['POST'])
def payment_details (request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    email = data_dict.get('email')

    user = User.objects.filter(email = email).first()

    if not user:
        return Response({'error':'User not found'},status= status.HTTP_204_NO_CONTENT)
    
    payments = Payment.objects.create(
        user = user,
        paid_using = data_dict.get('paid'),
        amount = data_dict.get('amount'),
        account_no = data_dict('account'),
        bank_name = data_dict.get('bank '),
    )
    payments.save()

    return Response({'message':'Payment Successfully done'}, status= status.HTTP_200_OK)
