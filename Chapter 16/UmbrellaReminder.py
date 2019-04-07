#! python3
# Chapter 16 Project - Scrape the weather for today and text if an umbrella is needed

import requests, bs4, smtplib, logging, TwilioCredentials
from twilio.rest import Client

# Make request to weather site
logging.info("1. Checking weather url")
url = 'https://weather.gc.ca/city/pages/bc-74_metric_e.html'
res = requests.get(url)
res.raise_for_status()

# Use Beautiful Soup to parse the html
logging.info("2. Parsing url html")
html = bs4.BeautifulSoup(res.text, 'lxml')
weatherClass = html.select_one('p .wxo-metric-hide').getText()

# Setup twilio
logging.info("3. Texting weather info")
accountSID = TwilioCredentials.credentials.get('sid')
authToken = TwilioCredentials.credentials.get('token')
myNumber = TwilioCredentials.credentials.get('myCellNumber')
twilioNumber = TwilioCredentials.credentials.get('myTwilioNumber')
message = "The weather today will be: %s" % weatherClass

twilioClient = Client(accountSID, authToken)
twilioClient.messages.create(body=message, from_=twilioNumber, to=myNumber)
logging.info("Done.")