from django.urls import path
from .views import inference


app_name = "isp_customer"


urlpatterns = [
    path('isp-customer/', view=inference, name='isp-customer-inference'),
]