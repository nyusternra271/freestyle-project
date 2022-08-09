from getpass import getpass
from pandas import read_csv, read_json, json_normalize
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
import requests
import json
import time
#import pandas
import os
import base64

from dotenv import load_dotenv

load_dotenv()




# get keys
#rapid_api_key = getpass("Please input your API key: ")
rapid_api_key = os.getenv("RAPID_API_KEY")
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
#print(response_json)

# View Data
prop_sale = json_normalize(data=response_json['results'])
print(response_json.keys())
print('Num of rows:', len(prop_sale))
print('Num of cols:', len(prop_sale.columns))
print(prop_sale)
# 
prop_sale_csv = prop_sale.to_csv(index=False)
print(prop_sale_csv)
message = Mail(
    from_email='razi.ahmad1@gmail.com',
    to_emails='razi.ahmad1@gmail.com',
    subject='Zillow Property Update',
    html_content='<strong>First row of data:</strong>')
base64_csv = base64.b64encode(prop_sale_csv.encode())


message.attachment = Attachment(FileContent(base64_csv.decode()),
                                    FileName('dataframe.csv'),
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
