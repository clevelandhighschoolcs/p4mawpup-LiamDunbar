# import libraries
import urllib2

#this code checks to make sure Beautiful Soup functions as planned. If not, the program stops instead of giving the user an error
try:
	from bs4 import BeautifulSoup
except Exception:
	print "Unless you have BeautifulSoup downloaded, this program won't function correctly. Use 'pip install BeautifulSoup4' to download it." 
	quit()

import csv
from datetime import datetime
import time
import re
import sys

def main():
    time1 = raw_input("How long do you want to search for in seconds? ")
    wait = raw_input("How long do you want to wait between searches in seconds? ")
    time2 = float(time1)
    while time2 > 1:
        # specify the url
        quote_page = 'https://www.investopedia.com/markets/stocks/intc/?ad=dirN&qo=investopediaSiteSearch&qsrc=0&o=40186'
        # query the website and return the html to the variable 'page'
        page = urllib2.urlopen(quote_page)
        # parse the html using beautiful soap and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')
        # get the index price
        price_box = soup.find('td', attrs={'id':'quotePrice'})
        price = price_box.text
        print price
        # open a csv file with append, so old data not be erased
        with open('index.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([price, datetime.now()])
        time2 -= float(wait)
        time.sleep(1)
	
main()
