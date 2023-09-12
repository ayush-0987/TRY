from django.db import models

# Create your models here.

class Address(models.Model):
    hno = models.IntegerField(null=False, primary_key=True)
    area = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField(null=False)
    country = models.CharField(max_length=50)

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)