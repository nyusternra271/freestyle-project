import requests
from dotenv import load_dotenv

import os
import json

load_dotenv()

api_key = os.getenv("API_KEY", default="OOPS, please set the API key")
print(api_key)
request_url = "https://zillow56.p.rapidapi.com/search"
query_string = { "location": "jamaica, ny"}
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

response = requests.request( "GET", request_url, headers=headers, params=query_string)

print(type(response.text))