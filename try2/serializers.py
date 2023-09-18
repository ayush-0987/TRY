from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Person, Family_details, Cart, Package

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family_details
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart 
        field = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Package
        field = '__all__'