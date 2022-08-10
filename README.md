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
2. A RapidAPI API key with a subscription to the Zillow API. <strong><em> Note that there are four plans available, including a free one (Basic). The Basic plan limits you to 30 API requests per month; each subsequent request costs $0.05. For testing purposes, the Basic plan should be sufficient.</em></strong>

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

