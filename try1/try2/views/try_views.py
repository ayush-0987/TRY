from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from try2.models import Address, Person
import json

@api_view(['POST'])
def information(request):
    if request.method == 'POST':
        data = request.body
        data_str = data.decode('utf-8')
        data_dict = json.loads(data_str)

        try:
            address = Address.objects.create(
                hno=data_dict['hno'],
                area=data_dict['area'],
                state=data_dict['state'],
                pincode=data_dict['pin'],
                country=data_dict['country'],
            )
            response_data = {
                'message': 'Address created successfully',
                'house_no': address.hno,
            }
            return JsonResponse(response_data, status=201)  # 201 Created status code
        
        except Exception as e:
            error_message = str(e)
            response_data = {'error': error_message}
            return JsonResponse(response_data, status=400)  # 400 Bad Request status code for errors

@api_view(['POST'])
def user_data(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    data_dict['address'] = Address.objects.all()
    
    details = Person.objects.create(
            
        first_name = data_dict['fname'],
        last_name = data_dict['lname'],
        gender = data_dict['gender'],
        address_id = data_dict['hno']
        
    )

    message = {"user details saved successfully"}
    return Response(message, status= status.HTTP_201_CREATED)

