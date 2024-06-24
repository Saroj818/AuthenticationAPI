# This is prototype of "Authentication APIS using REST Framework" application developed using Python's Django framework.

## This project is developed on Python 3.10.

### You can find the required packages in requirements.txt file. Please use below command to install the packages:
```bash
  pip install -r requirements.txt
```


### Please use the below command to run the project:
```bash 
    python manage.py runserver
```

### Below are the list of APIs available:
* **GET : http://127.0.0.1:8000/api/basic/auth** : API shows the usage of BasicAuthentication in Django using username and password.
* **POST : http://127.0.0.1:8000/api/token/auth** : API shows the usage of Django's TokenAuthentication. We retrieve token by validating using username and password. We pass the username and password in the body parameters as below:
            {"username":"admin",
            "password":"admin"} 
* **GET : http://127.0.0.1:8000/api/token/example** : API shows the usage of Django's TokenAuthentication. The token retrived from above POST request will be passed in the header's of this api to get the response.
* **POST : http://127.0.0.1:8000/api/jwt/token/** : API shows the usage of Django's JWT authentication. We retrieve token by validating using username and password. We pass the username and password in the body parameters as below:
            {"username":"admin",
            "password":"admin"} 
* **POST : http://127.0.0.1:8000/api/jwt/refresh/** : API shows the usage of Django's JWT authentication. We use refresh token and retreive a new access token. We pass the refresh token in the body parameters as below:
            {"refresh":"XXX.........XXX"} 
* **GET : http://127.0.0.1:8000/api/jwt/example** : API shows the usage of Django's JWT authentication. The token retrived from "api/jwt/token/" POST request will be passed in this api to get the response.
* **POST : http://127.0.0.1:8000/api/country** : API shows the utilization of Django's JWT authentication. The token retrived from "api/jwt/token/" POST request will be passed in this api to create the countries. Below data has to be passed into the body:
        { "name":"XYZ",
          "continent":"ABC",
          "population":"00000"}
* **GET : http://127.0.0.1:8000/api/country** : API shows the utilization of Django's JWT authentication. The token retrived from "api/jwt/token/" POST request will be passed in this api to get the list of all countries. 

Django Superadmin credentials (Username/pwd):
admin/admin

**POSTMAN COLLECTION IS ATTACHED IN THE PROJECT FOR REFERENCE.**
NOTE: This README.md is developed using Markdown. Please preview in Markdown for local viewing for best view.