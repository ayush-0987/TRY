from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from try2.models import Cart
from try2.serializers import CartSerializer
import json
from django.contrib.auth.models import User
from try2.models import Package,Person

@api_view(['GET'])
def get_all(request):
    cart = Cart.objects.all()
    serializer =CartSerializer(cart,many = True)
    message = {'info':'Cart items fetched successfully','data':serializer.data}
    return Response(message,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_items_as_per_user(request, pk):
    try:
        cart = Cart.objects.filter(user=pk)
        serializer = CartSerializer(cart, many= True)
        message = {'info':'Cart items fetched successfully','data':serializer.data}
        return Response(message,status=status.HTTP_200_OK)
    except Exception as e:
        message = {'error':str(e)}
        return Response(message, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def cart_items(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    email = data_dict.get('email')

    user = Person.objects.filter(email=email).first()
    
    name = data_dict.get('name')
    package = Package.objects.filter(name = name).first()
    print(data_dict)

    if not package:
        return Response({'error':'Package not found'}, status= status.HTTP_204_NO_CONTENT)
    
    price = package.price

    cart_item = Cart.objects.create(
        user = user,
        name = name,
        quantity = data_dict.get('quantity'),
        price = price,
    )
    cart_item.save()
    return Response({'message':'Items added to cart successfully'},status= status.HTTP_200_OK)

@api_view(['DELETE'])
def remove_item(request, id):
    try:
        cart = Cart.objects.filter(id=id)
        cart.delete()
        return Response({"message":"Item from cart removed Successfully"}, status= status.HTTP_200_OK)
    
    except Cart.DoesNotExist:        
        return Response({"error":"Item cannot be deleted"}, status=status.HTTP_204_NO_CONTENT)