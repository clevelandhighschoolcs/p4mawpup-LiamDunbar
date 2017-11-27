# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time
import re
import threading

def main():
	threading.Timer(10.0, main).start()
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
		writer.writerow([name, price, datetime.now()])
	
main()