import requests
from twilio.rest import Client

import datetime
import time

from bs4 import BeautifulSoup
import ast
import json



account_sid = 'YOUR_ACCOUNT_SID' #get from Twilio
auth_token = 'YOUR_AUTH_TOKEN' #get from Twilio
client = Client(account_sid, auth_token)

URL = "https://api.ontario.ca/api/drupal/page%2F2020-ontario-immigrant-nominee-program-updates?fields=nid,field_body_beta,body"
now = datetime.datetime.now()
length = 35557 # original str length of the current site

r = requests.get(URL)
dict = ast.literal_eval(json.dumps(json.loads(r.text), indent=2))
soup = BeautifulSoup(dict['body']['und'][0]['value'], 'lxml')

while True:
    if len(r.text.encode('utf-8')) > length:

        #send text message notification
        message = client.messages \
            .create(
            body="check the website!!  \n" + now.strftime("%Y-%m-%d %H:%M:%S")+"\nNew updates:"+soup.find_all('h3')[0].text,
            from_='+16470000000', # Phone number got from Twilio
            to='+16471111111' # Your phone number
        )
        print(message.sid)

        print("check website!!!!!!!   "+ now.strftime("%Y-%m-%d %H:%M:%S")+"\nNew updates:"+soup.find_all('h3')[0].text)

        length=len(r.text.encode('utf-8')) # update str length

    else:

        print("wait!  " + now.strftime("%Y-%m-%d %H:%M:%S")+"\nLast updated: "+soup.find_all('h3')[0].text) # show last modified date of the website

    time.sleep(60) # program runs every minute

