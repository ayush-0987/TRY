from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import json
from try2.models import Payment
from try2.serializers import PaymentSerializer  
import razorpay
from django.conf import settings
from django.shortcuts import redirect,render

@api_view(['GET'])
def get_all(request):
    payment = Payment.objects.all()
    serializer = PaymentSerializer(payment, many = True)
    return Response({'message':'Payments done by the user till now are'})

@api_view(['GET'])
def get_as_per_user(request, pk):
    try:
        payment = Payment.objects.filter(user = pk)
        serializer = PaymentSerializer(payment, many = True)
        return Response({'message':'payment made by the user are'},status=status.HTTP_302_FOUND)
    except:
        return Response({"error":"User not found"},status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def payment_details (request):
    data = json.loads(request.body.decode('utf-8'))

    email = data.get('email')

    user = User.objects.filter(email = email).first()

    if not user:
        return Response({'error':'User not found'},status= status.HTTP_204_NO_CONTENT)
    
    client = razorpay.Client(auth=("rzp_test_BA8h2fVuNo84v4", "rzp_test_BA8h2fVuNo84v4"))

    try:
        amount = int(data.get('amount'))*100
        order = client.order.create(
            amount = amount,
            currency = 'INR',
        )   

        payments = Payment.objects.create(
            user = user,
            paid_using = data.get('paid'),
            amount = amount,
            account_no = data.get('account'),
            bank_name = data.get('bank '),
            razorpay_order_id = order['id']
        )

        return Response({'order_id': order['id'], 'amount': amount, 'currency': 'INR'})
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)