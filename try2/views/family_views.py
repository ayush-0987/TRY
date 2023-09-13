from try2.models import Family_details, Person
from rest_framework.decorators import api_view
from try2.serializers import FamilySerializer
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['GET'])
def get_all(request):
    family = Family_details.objects.all()
    serializer = FamilySerializer(family,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_userfamily(request, pk):
    try:
        family = Family_details.objects.filter(family_head = pk)
        serializer = FamilySerializer(family, many = True)
        message = {'Info':'Family Members associated with this user are as follows:', 'data':serializer.data}
        return Response(message,status=status.HTTP_200_OK)

    except:
        message = {'Error':'No such User exists'}
        return Response(message,status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def add (request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)
    
    head = Person.objects.filter(email = data_dict['family_head']).first()

    family_member = Family_details.objects.create(
        name = data_dict['name'],
        relation = data_dict['relation'],
        gender = data_dict['gender'],
        anniversary_date = data_dict['anniversary'],
        date_of_birth = data_dict['dob'],
        family_head = head
    )

    serializer = FamilySerializer(family_member)
    message = {
        'Info' : 'Family member added successfully',
        'family': serializer.data
    }
    return Response(message, status= status.HTTP_201_CREATED)