from django.contrib import admin
from .models import Person, Address, Family_details, AddressBasic

# Register your models here.

admin.site.register(Person)
admin.site.register(Address)
admin.site.register(AddressBasic)
admin.site.register(Family_details)