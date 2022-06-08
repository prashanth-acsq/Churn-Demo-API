import math
import pickle
import numpy as np

import warnings
warnings.filterwarnings("ignore")


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def clean_data(old_data: str) -> np.ndarray:
    old_data = [data for data in old_data.split(",")]
    new_data = []
    for d in old_data:
        if "[" in d: d = d.replace("[", "")
        if "]" in d: d = d.replace("]", "")
        new_data.append(float(d))
    return np.array(new_data).reshape(1, -1)


def infer_churn_probability(data: np.ndarray, mode: str) -> tuple:
    if mode == "bank": model = pickle.load(open("static/models/bank-customer-churn-model.pkl", "rb"))
    elif mode == "isp": model = pickle.load(open("static/models/isp-customer-churn-model.pkl", "rb"))

    y_pred = model.predict(data)[0]
    y_pred_proba = model.predict_proba(data)[0][1]

    if y_pred == 0: 
        return "Not Exited", y_pred_proba
    else: 
        return "Exited", y_pred_proba
