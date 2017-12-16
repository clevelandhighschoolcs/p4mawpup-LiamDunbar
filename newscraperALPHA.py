#THIS IS STILL A WORK IN PROGRESS IT PROBABLY WONT WORK YET

# import libraries
import urllib2
from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import csv
from datetime import datetime
import time
import re
import sys

accountsid = ''
authtoken = ''
twiliophonenumber = ''
myphonenumber = ''

try:
	from bs4 import BeautifulSoup
except Exception:
	print "Unless you have BeautifulSoup downloaded, this program won't function correctly. Use 'pip install BeautifulSoup4' to download it." 
	quit()

def main():
    time1 = raw_input("How long do you want to search for in seconds? ")
    wait = raw_input("How long do you want to wait between searches in seconds? ")
    time2 = float(time1)
    while time2 > 1:
        quote_page = raw_input("Paste URL Here:")
        page = urllib2.urlopen(quote_page)
        data = page.read()
        datastring = str(data)
        lengthB = len(datastring)
        time = 0
        soup = BeautifulSoup(page, 'html.parser')
        price_box = soup.find('td', attrs={'id':'quotePrice'})
        price = price_box.text
        if time1 == 0:
        		while True:
        			page = urllib2.urlopen(quote_page)
        			data = page.read()
        			datastring = str(data)
        			lengthA = len(datastring)
        			if lengthB != lengthA:
        				print price
                        body= price
                        Client = Client(accountsid, authtoken)
                        Client.messages.create(
                            body=body,
                            to=myphone,
                            from_=twiliophone
                            )
        with open('index.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([price, datetime.now()])
        time2 -= float(wait)
        time.sleep(1)

main()
