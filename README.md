# Python 2335 Summer 2022 Freestyle Project

## Team Members
- Razi Ahmad
- Misbah Talha
- Chris Mahadeo
- Michael Noah

## How it Works

This app sends a list of properties for sale in a particular city where there's been a price drop. It takes 3 inputs:
- City
- State
- Email Address

## Prerequisites
In order to run this code, you'll need the following:

1. A SendGrid API key
<br><br>
Follow these steps to sign up for a SendGrid API key:

    1. Go to https://signup.sendgrid.com and register using an email address of your choosing (using a Gmail account is recommended due to possible issues with school or employer email domains)
    2. Follow the instructions to complete the "Single Sender Verification" by clicking the link in the confirmation email you received (remember to check your spam folder if you don't see this email in a timely fashion). You can also access this utility via the Settings menu (Settings->Sender Authentication) from your dashboard after logging in.

    <strong><em>Note that you must copy the API key once this verification step is done, as SendGrid does not display the key afterwards. If you fail to do so, you'll need to delete the key and create a new one from the Settings menu on the dashboard (Settings->API Keys)</em></strong>
2. A RapidAPI API key with a subscription to the Zillow API. 
<br><strong><em> Note that there are four plans available, including a free one (Basic). The Basic plan limits you to 30 API requests per month; each subsequent request costs $0.05. For testing purposes, the Basic plan should be sufficient.</em></strong>
<br>
<br>
To sign up for an RapidAPI key, follow these steps:

    1. Browse to https://rapidapi.com and create an account
    2. Create a new app from the developer dashboard (https://rapidapi.com/developer/dashboard). An API key is automatically generated:
    <br>
    ![RapidAPI API Key Screenshot](https://github.com/nyusternra271/miscellaneous/blob/main/rapidapi-key-screenshot.png)
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

