from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class AddressBasic(models.Model):
    id = models.AutoField(primary_key= True)
    society = models.CharField(max_length=20)
    area = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField(null=False)
    country = models.CharField(max_length=50)
    
class Address(models.Model):
    hno = models.IntegerField(null=False, primary_key=True)
    floor = models.IntegerField(null=True)
    block = models.CharField(max_length=5,null=True)
    basic = models.ForeignKey(AddressBasic, on_delete=models.CASCADE)

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    hno = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_of_birth = models.DateField(auto_now=False,null=False)
    marital_status = models.CharField(max_length=20,null=False)
    email = models.EmailField(null=False)
    is_verified = models.BooleanField(default=False)
    parties = models.CharField(max_length=10, choices=(('owner','owner'),('tenant','tenant')), default='owner')

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    
class Family_details(models.Model):
    family_head = models.ForeignKey(Person, on_delete=models.CASCADE)
    relation = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    anniversary_date = models.DateField(auto_now=False,null=True)
    date_of_birth = models.DateField(auto_now=False,null=False)
    
    def __str__(self):
        return f"{self.name}"

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, null=False,blank=False)
    name = models.CharField(max_length=12)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    
class Order(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    item_details = models.CharField(max_length=100)
    price = models.OneToOneField(Cart, on_delete=models.CASCADE)
    done_payment = models.BooleanField()
    
class Payment(models.Model):
    paid_using_choices = [
    ('cash', 'Cash'),
    ('online', 'Online'),
    ('NEFT', 'NEFT'),
    ('RTGS', 'RTGS'),
]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    paid_using = models.CharField(max_length=10, choices=paid_using_choices, default='')
    account_no = models.BigIntegerField(null=True, blank=True)
    bank_name = models.CharField(max_length=19, null=True, blank= True)
    payment_date = models.DateTimeField(auto_now=True, null=False, blank=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    reference_id = models.ForeignKey(Order, on_delete=models.CASCADE)

class Package(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.IntegerField()
    no_of_users = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    available_for = models.CharField(max_length=10, choices=(('owner','owner'),('tenant','tenant')), default='owner')   