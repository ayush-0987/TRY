from django.urls import path
from try2.views import add_user_views as views

urlpatterns = [
    path('add/', views.user_data, name = 'add_user')
]