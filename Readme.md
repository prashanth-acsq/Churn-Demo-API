## **Customer Churn Demo API**

<br>

- Uses `python-3.8.10`
- API built using Django
- Local hosting at `http://127.0.0.1:10001`
- Only works if locally hosted
- Endpoints Available
    - `/bank-customer/`
    - `/isp-customer/`

<br>

### **Detailed Information**

<br>

1. Install `python 3.8.x`
2. Run `pip install virtualenv`
3. Run `make-env.bat`
4. Run `start-local-server.bat`. The API will now be served at `http://127.0.0.1:10001`
5. Run `run-test.bat` to verify that the API works properly
6. To run in production mode
    - Change `DEBUG` to `False` in Main.settings
    - Ensure appropriate environment variable is set
    - Run `collect-static.bat` before `start-server.bat` 

<br>

### **Notes on Models**

<br>

<pre>
Bank - GBC, F2
ISP  - RFR, F3
</pre>

