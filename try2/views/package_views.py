from rest_framework.decorators import api_view
from rest_framework.response import Response
from try2.models import Package
import json
from rest_framework import status
from try2.serializers import PackageSerializer

@api_view(['GET'])
def get_all(request):
    package = Package.objects.all()
    serializer = PackageSerializer(package, many= True)
    message = {'info':'Package details fetched successfully','data': serializer.data}
    return Response(message, status= status.HTTP_200_OK)

@api_view(['GET'])
def get_package_details (request,pk):
    try:
        Package = Package.objects.filter(User= pk)
        serializer = PackageSerializer(Package, many = True)
        message = {'info':'Package details of the user are:','data':serializer.data}
        return Response(message, status=status.HTTP_303_SEE_OTHER)

    except Exception as e:
        message = {'error':str(e)}
        return Response(message, status= status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def add_package(request):
    try:
        data = request.body
        data_str = data.decode('utf-8')
        data_dict = json.loads(data_str)

        if 'details' not in data_dict:
            return Response({'error': 'Details field is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        name = data_dict.get('name')

        package = Package.objects.filter(name = name).first()
        if package :
            return Response({'error':'package with this name already exists'}, status = status.HTTP_302_FOUND)

        add_packages = Package.objects.create(
            name = name,
            details = data_dict.get ('details'),
            price = data_dict.get('price'),
            period = data_dict.get('period'),
            no_of_users =data_dict.get('users'),
            available_for = data_dict['for'],
        )
        add_packages.save()
        return Response({'message':'Package details added Successfully'}, status=status.HTTP_200_OK)
    
    except:
        return Response({'error':'Package addition Unsuccessful'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['DELETE'])
def remove_package(request, id):
    try:
        package = Package.objects.get(id= id)
        package.delete()
        return Response({'message':'Package removed Successfully'}, status=status.HTTP_200_OK)
    
    except:
        return Response({'error':'Package cannot be removed or Package not found '}, status= status.HTTP_404_NOT_FOUND)
