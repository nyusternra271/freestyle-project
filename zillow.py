from getpass import getpass
from pandas import read_csv, read_json
from plotly.express import line
import requests
import json
import time
import pandas


# get keys
rapid_api_key = getpass("Please input your API key: ")
city = input("Please enter a city in: ")
state = input("Please enter a state: ")
search_str = city + ', ' + state
print('Search string:', search_str)





#c7fe818c2amshbc9b51c74fe5a8ep1983d3jsn15c748e613b8
#https://zillow56.p.rapidapi.com/search

url = "https://zillow56.p.rapidapi.com/search"

querystring = {"location":search_str,
               "home_type":"Houses",
               "minPrice":"500000",
               "maxPrice":"2000000"

               
               }

headers = {
	"X-RapidAPI-Key": rapid_api_key,
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}


response = requests.request("GET", url, headers=headers, params=querystring)

response_json = response.json()
response_json

# View Data
prop_sale = pandas.json_normalize(data=response_json['results'])
print('Num of rows:', len(prop_sale))
print('Num of cols:', len(prop_sale.columns))
prop_sale
# 