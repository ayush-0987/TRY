from django.urls import path
from try2.views import payment_views as views

urlpatterns = [
    path('details/', views.payment_details, name = 'payment-details')
]