from django.urls import path
from .views import inference


app_name = "bank_customer"


urlpatterns = [
    path('bank-customer/', view=inference, name='bank-customer-inference'),
]