from django.contrib import admin
from .models import Person, Address, Family_details, AddressBasic, Cart, Order, Payment, Package

admin.site.register(Person)
admin.site.register(Address)
admin.site.register(AddressBasic)
admin.site.register(Family_details)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Package)