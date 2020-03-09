import requests
from twilio.rest import Client

import datetime
import time

from bs4 import BeautifulSoup
import ast
import json



account_sid = 'AC6b3b47753df22c7067c6ea62a29b3d83'
auth_token = '1f35d8f2e5105678191cd68ef1b5924d'
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

# print(r.text) #str
# print(json.dumps(json.loads(r.text), sort_keys=True, indent=4)) #str

# urllib
# request = Request(URL,headers=s)
# json_r = urlopen(request).read() #.decode()
# print(json_r)


# header
# s = {'Host': ' api.ontario.ca',
#      'Connection': 'keep-alive',
#      'Accept': 'application/json, text/plain, */*',
#      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
#      'Origin': 'https://www.ontario.ca',
#      'Sec-Fetch-Site': 'same-site',
#      'Sec-Fetch-Mode': 'cors',
#      'Referer': 'https://www.ontario.ca/page/2020-ontario-immigrant-nominee-program-updates',
#      'Accept-Encoding': 'gzip, deflate, br',
#      'Accept-Language': 'en-CA,en;q=0.9,zh-CN;q=0.8,zh-HK;q=0.7,zh;q=0.6,en-GB;q=0.5,en-US;q=0.4,zh-TW;q=0.3'}

# https://www.ontarioimmigration.gov.on.ca/register_enu/dynamicform//register/enu
#
# GET /register_enu/dynamicform//register/enu HTTP/1.1
# Host: www.ontarioimmigration.gov.on.ca
# Connection: keep-alive
# Cache-Control: max-age=0
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
# Sec-Fetch-User: ?1
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Sec-Fetch-Site: same-origin
# Sec-Fetch-Mode: navigate
# Referer: https://www.ontarioimmigration.gov.on.ca/register_enu/dynamicform/register/start?oinpToken=01179d2b-47a2-4c44-a007-94bcf21a8af1&lang=en
# Accept-Encoding: gzip, deflate, br
# Accept-Language: en-CA,en;q=0.9,zh-CN;q=0.8,zh-HK;q=0.7,zh;q=0.6,en-GB;q=0.5,en-US;q=0.4,zh-TW;q=0.3
# Cookie: _ga=GA1.3.896969725.1583440964; _gid=GA1.3.119352809.1583440964; CFJSESSIONID=0000t54_JW4xv-M2p3-OjcTUY6S:1bd1v4e62; AUTH_SESSION_ID=SMS_csbbigdcapmdw08_f68cd6::72e17ba69c0bd52ff012317a019eff53