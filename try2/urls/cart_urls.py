from django.urls import path
from try2.views import cart_views as views

urlpatterns= [
    path('all/',views.get_all, name = 'get all cart items'),
    path('<str:pk>',views.get_items_as_per_user, name='user items'),    
    path('add/', views.cart_items, name= 'add items to cart'),
    path('<str:id>/dlt/', views.remove_item, name='remove-item'),
]
