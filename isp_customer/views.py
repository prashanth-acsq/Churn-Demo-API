import json
import numpy as np

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from static.utils import infer_churn_probability, clean_data


@csrf_exempt
def inference(request):
    if request.method == "POST":
        if request.POST.get("web_client_data") is not None:
            JSONData = request.POST.get("web_client_data")

            is_tv_subscriber = float(json.loads(JSONData)["is_tv_subscriber"])
            is_movie_package_subscriber = float(json.loads(JSONData)["is_movie_package_subscriber"])
            subscription_age = float(json.loads(JSONData)["subscription_age"])
            bill_avg = float(json.loads(JSONData)["bill_avg"])
            remaining_contract = float(json.loads(JSONData)["remaining_contract"])
            service_failure_count = float(json.loads(JSONData)["service_failure_count"])
            download_avg = float(json.loads(JSONData)["download_avg"])
            upload_avg = float(json.loads(JSONData)["upload_avg"])
            download_over_limit = float(json.loads(JSONData)["download_over_limit"])
            
            new_data = np.array([is_tv_subscriber, 
                                 is_movie_package_subscriber, 
                                 subscription_age, 
                                 bill_avg,
                                 remaining_contract, 
                                 service_failure_count, 
                                 download_avg, 
                                 upload_avg,
                                 download_over_limit]).reshape(1, -1)

        else:
            old_data = request.POST.get("python_client_data")
            new_data = clean_data(old_data)
            del old_data

        label, prob = infer_churn_probability(new_data, "isp")
        
        return JsonResponse({
            "label": label,
            "probability" : str(prob),
        })

    return HttpResponse("ISP Customer Churn Probability Inference Endpoint")
