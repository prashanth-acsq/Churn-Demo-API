import sys
import requests
import random as r


def breaker(num: int=50, char: str="*") -> None:
    print("\n" + num*char + "\n")


def main():

    args = "--num"
    num_of_samples: int = 10
    
    if args in sys.argv: num_of_samples = int(sys.argv[sys.argv.index(args) + 1])

    response = requests.request(method="GET", url="http://127.0.0.1:10001/")
    if response.status_code == 200: 
        assert response.text == "Churn Prediction - Root URL"
    else: print(f"Error, {response.status_code} - {response.reason}")

    endpoints = ["bank-customer", "isp-customer"]

    for endpoint in endpoints:
        response = requests.request(method="GET", url=f"http://127.0.0.1:10001/{endpoint}")
        if response.status_code == 200:
            if endpoint.split("-")[0] == "bank":
                assert response.text == "Bank Customer Churn Probability Inference Endpoint"
            elif endpoint.split("-")[0] == "isp":
                assert response.text == "ISP Customer Churn Probability Inference Endpoint"
        else: print(f"Error, {response.status_code} - {response.reason}")

        if endpoint.split("-")[0] == "bank":
            data = {
                    "python_client_data" : str([900, 0, 1, 29, 4, 29000, 0, 1, 1, 120000]).encode("utf-8"),
                }
            response = requests.request(method="POST", url=f"http://127.0.0.1:10001/{endpoint}/", data=data)
        
            if response.status_code == 200: 
                # print(f"Probability of Exit : {float(response.json()['probability']):.2f}")
                assert float(response.json()['probability']) >= 0.0 and float(response.json()['probability']) <= 0.1

        elif endpoint.split("-")[0] == "isp":
            data = {
                    "python_client_data" : str([0, 1, 4, 1000, 4, 8, 3000, 128, 5]).encode("utf-8"),
                }
            response = requests.request(method="POST", url=f"http://127.0.0.1:10001/{endpoint}/", data=data)
        
            if response.status_code == 200: 
                # print(f"Probability of Exit : {float(response.json()['probability']):.2f}")
                assert float(response.json()['probability']) >= 0.0 and float(response.json()['probability']) <= 0.36
        
        breaker()

        if endpoint.split("-")[0] == "bank":
            print("Bank Customers")
            breaker()

            for _ in range(num_of_samples):
                data = {
                    "python_client_data" : str([
                        r.randint(0, 2500), 
                        r.randint(0, 2), 
                        r.randint(0, 1), 
                        r.randint(18, 95), 
                        r.randint(0, 20), 
                        r.randint(0, 100000), 
                        r.randint(0, 2), 
                        r.randint(0, 1), 
                        r.randint(0, 1), 
                        r.randint(25000, 250000)]).encode("utf-8"),
                }

                response = requests.request(method="POST", url=f"http://127.0.0.1:10001/{endpoint}/", data=data)
                if response.status_code == 200: 
                    print(f"Probability of Exit : {float(response.json()['probability']):.2f}")
                else: print(f"Error, {response.status_code} - {response.reason}")

        elif endpoint.split("-")[0] == "isp":
            print("ISP Customers")
            breaker()

            for _ in range(num_of_samples):
                data = {
                    "python_client_data" : str([
                        r.randint(0, 1), 
                        r.randint(0, 1), 
                        r.uniform(0, 15), 
                        r.uniform(0, 2000), 
                        r.uniform(0, 4), 
                        r.randint(0, 20), 
                        r.uniform(0, 100000), 
                        r.uniform(0, 10000), 
                        r.randint(0, 10)]).encode("utf-8"),
                }

                response = requests.request(method="POST", url=f"http://127.0.0.1:10001/{endpoint}/", data=data)
                if response.status_code == 200: 
                    print(f"Probability of Exit : {float(response.json()['probability']):.2f}")
                else: print(f"Error, {response.status_code} - {response.reason}")
        
        breaker()


if __name__ == "__main__":
    sys.exit(main() or 0)
