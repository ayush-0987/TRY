from django.urls import path
from try2.views import order_views as views

urlpatterns = [
    path('all/', views.get_all, name= 'get-all-order'),
    path('<str:pk>',views.get_details_of_user, name = 'details-as-per-user'),
    path('place/', views.order_details, name = 'order-details'),
]
