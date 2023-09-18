from django.urls import path
from try2.views import package_views as views

urlpatterns = [
    path('all/', views.get_all, name = 'get-all-package'),
    path('<str:pk>', views.get_package_details, name = 'get-package-details'),
    path('add/', views.add_package, name = 'add-package'),
    path('<str:id>/dlt/',views.remove_package, name = 'remove-package')
]