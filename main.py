import requests as Requests

BASE_URL = 'https://fakestoreapi.com' # Constant

Response = Requests.get(f"{BASE_URL}/products")
print(Response.status_code)
