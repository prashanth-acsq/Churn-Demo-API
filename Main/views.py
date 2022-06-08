from django.http import HttpResponse


def index(request):
    return HttpResponse("Churn Prediction - Root URL")