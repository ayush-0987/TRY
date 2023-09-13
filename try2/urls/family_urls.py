from django.urls import path
from try2.views import family_views as views

urlpatterns = [
    path('', views.get_all, name='get_all_members'),
    path('<str:pk>', views.get_userfamily, name='get_userfamily'),
    path('add/', views.add, name= 'add'),
]