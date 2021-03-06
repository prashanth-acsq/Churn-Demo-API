from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('bank_customer.urls')),
    path('', include('isp_customer.urls')),
]
