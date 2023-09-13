from django.urls import path
from try2.views import add_user_views as views

urlpatterns = [
    path('', views.get_all, name = 'get_all_user_details'),
    path('<str:pk>', views.get_specified_user, name ='get_specified_user'),
    path('add/', views.user_data, name = 'add_user'),
]