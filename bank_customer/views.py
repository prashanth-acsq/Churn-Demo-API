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

            credit_score = float(json.loads(JSONData)["credit_score"])
            country = float(json.loads(JSONData)["country"])
            gender = float(json.loads(JSONData)["gender"])
            age = float(json.loads(JSONData)["age"])
            tenure = float(json.loads(JSONData)["tenure"])
            balance = float(json.loads(JSONData)["balance"])
            num_of_products = float(json.loads(JSONData)["num_of_products"])
            has_credit_card = float(json.loads(JSONData)["has_credit_card"])
            is_active_member = float(json.loads(JSONData)["is_active_member"])
            estimated_salary = float(json.loads(JSONData)["estimated_salary"])
            
            new_data = np.array([credit_score, 
                                 country, 
                                 gender, 
                                 age,
                                 tenure, 
                                 balance, 
                                 num_of_products, 
                                 has_credit_card,
                                 is_active_member, 
                                 estimated_salary]).reshape(1, -1)

        else:
            old_data = request.POST.get("python_client_data")
            new_data = clean_data(old_data)
            del old_data

        label, prob = infer_churn_probability(new_data, "bank")
        
        return JsonResponse({
            "label": label,
            "probability" : str(prob),
        })

    return HttpResponse("Bank Customer Churn Probability Inference Endpoint")
