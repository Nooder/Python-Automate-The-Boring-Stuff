#! python3
# Chapter 16 Project - Defines a textMyself() function that texts a message
#                      passed to it as a string

import TwilioCredentials
from twilio.rest import Client

# Setup
accountSID = TwilioCredentials.credentials.get('sid')
authToken = TwilioCredentials.credentials.get('token')
myNumber = TwilioCredentials.credentials.get('myCellNumber')
twilioNumber = TwilioCredentials.credentials.get("myTwilioNumber")

# Send message to myNumber
def textMyself(message):
    twilioClient = Client(accountSID, authToken)
    twilioClient.messages.create(body=message, from_=twilioNumber, to=myNumber)

# Test
textMyself("First test text message :)")
print("Done.")