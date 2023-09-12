from django.urls import path
from try2.views import try_views as views

urlpatterns = [
    path('mation/', views.information, name='address_field'),
    path('details/', views.user_data, name='user_data')
]