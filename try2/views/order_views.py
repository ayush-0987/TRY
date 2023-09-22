from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from try2.models import Order
from django.contrib.auth.models import User 
from try2.serializers import OrderSerializer

@api_view(['GET'])
def get_all(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response ({'message':'Details of all the orders done till now'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_details_of_user(request,pk):
    try:            
        order = Order.objects.filter(user = pk)
        serializer = OrderSerializer(order,many = True)
        return Response({'message':'order details of the user are'},status=status.HTTP_302_FOUND)
    
    except:
        return Response({'error':'User not found or order details cannot be fetched'},status=status.HTTP_303_SEE_OTHER)

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