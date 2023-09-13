from django.http import JsonResponse
from rest_framework.decorators import api_view
from try2.models import Address, AddressBasic
import json


@api_view(['POST'])
def user_address(request):
    if request.method == 'POST':
        data = request.body
        data_str = data.decode('utf-8')
        data_dict = json.loads(data_str)

        try:
            address = Address.objects.create(
                hno=data_dict['hno'],
                basic = AddressBasic.objects.filter(id = data_dict['basic_id']).first(),
                floor = data_dict['floor'],
                block = data_dict['block'],


                # area=data_dict['area'],
                # state=data_dict['state'],
                # pincode=data_dict['pin'],
                # country=data_dict['country'],
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