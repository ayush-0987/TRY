from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from try2.models import Order
from django.contrib.auth.models import User 

@api_view(['POST'])
def order_details(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    email = data_dict.get('email')

    user = User.objects.filter(email = email).first()

    if 'price' in data_dict:
        price = data_dict['price']
    else:
        price = None 

    order_detail = Order.objects.create(
        user = user,
        item_details = data_dict.get('item'),
        price = price,
        done_payment = data_dict.get('payment')
    )

    order_detail.save()
    return Response({'message':'Order successful'},status=status.HTTP_200_OK)