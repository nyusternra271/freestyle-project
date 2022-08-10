# Real State Price Alert via Email

## Team Members
- Razi Ahmad
- Misbah Talha
- Chris Mahadeo
- Michael Noah

## How it Works

This app sends a list of properties for sale in a particular city where there's been a price drop. The data comes from Zillow via an API from RapidAPI. It takes 3 inputs:
- City
- State
- Email Address

It returns listings that have been on Zillow ("Days on Zillow") for 90 days.

## Prerequisites
In order to run this code, you'll need the following:

1. A SendGrid API key
<br><br>
Follow these steps to sign up for a SendGrid API key:

    1. Go to https://signup.sendgrid.com and register using an email address of your choosing (using a Gmail account is recommended due to possible issues with school or employer email domains)
    2. Follow the instructions to complete the "Single Sender Verification" by clicking the link in the confirmation email you received (remember to check your spam folder if you don't see this email in a timely fashion). You can also access this utility via the Settings menu (Settings->Sender Authentication) from your dashboard after logging in.

    <strong><em>Note that you must copy the API key once this verification step is done, as SendGrid does not display the key afterwards. If you fail to do so, you'll need to delete the key and create a new one from the Settings menu on the dashboard (Settings->API Keys)</em></strong>
2. A RapidAPI API key with a subscription to the Zillow API. To sign up for an RapidAPI key, follow these steps:

    1. Browse to https://rapidapi.com and create an account
    2. Create a new app from the developer dashboard (https://rapidapi.com/developer/dashboard). An API key is automatically generated:
    
    ![RapidAPI API Key Screenshot](https://github.com/nyusternra271/miscellaneous/blob/main/rapidapi-key-screenshot.png)
    
    3. Click on the eye icon to reveal the API key. Make a copy and put it in your .env file in step 4 of the setup instructions below.
    4. Subscribe to the Zillow API here: https://rapidapi.com/s.mahmoud97/api/zillow56/
<br><strong><em> Note that there are four plans available, including a free one (Basic). The Basic plan limits you to 30 API requests per month; each subsequent request costs $0.05. For testing purposes, the Basic plan should be sufficient.</em></strong>
## Setup Instructions

1. Set up a new Anaconda environment:
```sh
conda create -n zillow-project python=3.10
```
2. Activate the new environment:
```sh
conda activate zillow-project
```
3. After cloning the repository, browse to the directory to which the repo files are saved and install the required packages:

```sh
pip install -r requirements.txt
```

4. In the main directory, create a file named .env; this file will contain your API keys for Sendgrid and the Zillow API. Your .env file should resemble the following:
```sh
RAPID_API_KEY="Rapid API Key"
SENDGRID_API_KEY="SendGrid API Key"
```
adding your API keys to the respective lines.

## Running the App

After going through the setup instructions above, you can run the application by running the following command:

```sh
python zillow.py
```
You should see something that resembles the screenshot below:

![Zillow App Screenshot](https://github.com/nyusternra271/miscellaneous/blob/main/run-zillow-app-screenshot.png)

You will also get an email with a CSV file named 'property_listings.csv' attached. Check your spam folder if you don't see the message in your inbox. The email will look like the following:

![Zillow App Email](https://github.com/nyusternra271/miscellaneous/blob/main/zillow_app_email.png)

<strong><br><em>Note that you may encounter a KeyError stating that one or more dataframe keys are not in the index depending on the city you search for. Some things you might want to try include:

1. Searching for a different city
2. Adjusting the Days on Zillow value (the "doz" key in the queryString dictionary in the code 
</em></strong>
