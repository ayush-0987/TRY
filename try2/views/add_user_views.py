from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from try2.models import Address, Person
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from try2.serializers import PersonSerializer
from django.http import HttpResponse
import json


def get_all(request):
    user = Person.objects.all()
    serializer = PersonSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_specified_user(request, pk):
    try:    
        user = Person.objects.get(id = pk)
        serializer = PersonSerializer(user, many = False)
        message = {'Info':'User details fetched successfully', 'data':serializer.data}
        return Response(message, status=status.HTTP_200_OK)
    except:
        message = {'error':'User not found or user not registered'}
        return Response(message, status=status.HTTP_303_SEE_OTHER)
    
@api_view(['POST'])
def user_data(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    data_dict['address'] = Address.objects.all()

    try:
        email = data_dict['email']
        user = User.objects.filter(email = email).first()

        if user:
            return Response({"error":"user with this email already exists"}, status= status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create(
            first_name = data_dict['fname'],
            last_name = data_dict['lname'],
            username = email,
            email = email,
            password = make_password(data_dict['password'])
        )
        
        details = Person.objects.create(
            user = user,
            email= email,                
            first_name = data_dict['fname'],
            last_name = data_dict['lname'],
            gender = data_dict['gender'],
            hno_id = data_dict['hno'],
            date_of_birth = data_dict['dob'],
            marital_status = data_dict['status'],
            parties = data_dict['party']
        )

        message = {"user details saved successfully"}
        return Response(message, status= status.HTTP_201_CREATED)
    
    except Exception as e:
        message = {"error":str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    data = request.body 
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    email = data_dict.get('email')
    password = data_dict.get('password')

    person = Person.objects.get(email= email)

    try:
        user = User.objects.get(email = email)
        if not user.check_password(password):
            return Response({"error":"Invalid Credentials: User ID or Password may be incorrect"}, status= status.HTTP_401_UNAUTHORIZED)
        
    except User.DoesNotExist:
        return Response({"error":"User not found"}, status= status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({'error':str(e)})
    
    return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
