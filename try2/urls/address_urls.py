from django.urls import path
from try2.views import address_views as views

urlpatterns= [
    path('address/',views.user_address, name = 'user_address')
]
