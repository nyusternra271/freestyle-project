from getpass import getpass
from pandas import read_csv, read_json, json_normalize
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId, To)
import requests
import json
import time
#import pandas
import os
import base64

from dotenv import load_dotenv

load_dotenv()

print("WELCOME REAL ESTATE INVESTOR")

print("-------------------")

rapid_api_key = os.getenv("RAPID_API_KEY")
city = input("Please enter a city: ")
state = input("Please enter a state: ")
recipient_address = input("Please enter your email address:")
search_str = city + ', ' + state
print('Search string:', search_str)

url = "https://zillow56.p.rapidapi.com/search"

querystring = {"location":search_str,
               "home_type":"Houses",
               "minPrice":"500000",
               "maxPrice":"2000000",
                "doz": "90"
               
               }

headers = {
	"X-RapidAPI-Key": rapid_api_key,
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}


response = requests.request("GET", url, headers=headers, params=querystring)

response_json = response.json()
#print(response_json)

# View Data
prop_sale = json_normalize(data=response_json['results'])
if prop_sale.empty:
    print('No results returned')
    exit()

#print('Num of rows:', len(prop_sale))
#print('Num of cols:', len(prop_sale.columns))

prop_sale_subset = prop_sale[['country','state', 'city', 'zipcode' , 'streetAddress', 'homeType', 'price','lotAreaValue', 'livingArea', 'bathrooms', 'bedrooms', 'taxAssessedValue', 'rentZestimate', 'priceChange', 'priceReduction']]

prop_sale_filtered = prop_sale_subset.dropna(subset=['priceReduction'])
print(prop_sale_filtered)
prop_sale_csv = prop_sale_filtered.to_csv(index=False)
message = Mail(
    from_email='razi.ahmad1@gmail.com',
    to_emails=recipient_address,
    subject='Zillow Property Update',
    html_content=f"<h2>Please see the attached file for a list of properties in {city}, {state} with a drop in price</h2>")
base64_csv = base64.b64encode(prop_sale_csv.encode())


message.attachment = Attachment(FileContent(base64_csv.decode()),
                                    FileName('property_listings.csv'),
                                    FileType('text/csv'),
                                    Disposition('attachment'),
                                    ContentId('datafrane'))
print(type(message))
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
