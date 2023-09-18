from django.urls import path
from try2.views import order_views as views

urlpatterns = [
    path('place/', views.order_details, name = 'order-details'),
]
