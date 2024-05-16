import requests as Requests
import pandas as Pandas

BASE_URL = 'https://fakestoreapi.com' # Constant

Response = Requests.get(f"{BASE_URL}/products")
JsonContent = Pandas.DataFrame(Response.json())

with open('ResponseData.csv', 'w', newline='') as File:
    File.write(JsonContent.to_csv())
    pass
