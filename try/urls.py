"""
URL configuration for try1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    # path('jet/', include('jet.urls','jet')),
    path('admin/', admin.site.urls),
    path('api/family/', include('try2.urls.family_urls')),
    path('api/info/', include('try2.urls.add_user_urls')),
    path('api/address/', include('try2.urls.address_urls')),
    path('api/cart/', include('try2.urls.cart_urls')),
    path('api/package/', include('try2.urls.package_urls')),
    path('api/order/',include('try2.urls.order_urls')),
    path('api/payment/',include('try2.urls.payment_urls')),
]
