#example from https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

#import libraries
import urllib2
from bs4 import BeautifulSoup

#specify url
quote_page = ['http://www.bloomberg.com/quote/SPX:IND', 'https://www.bloomberg.com/quote/CCMP:IND']

#for loop
data = []
for pg in quote_page:
  #query the website and return the html to the var page
  page = urllib2.urlopen(pg) #urlopen module interface for fetching data across the web
  #parse the html using beautiful soup an store in var soup
  soup = BeautifulSoup(page, 'html.parser')

  # remove div of name and get its value
  name_box = soup.find('h1', attrs={'class': 'name'})
  name = name_box.text.strip() #strip() removes starting and trailing

  #get the index price
  price_box = soup.find('div', attrs={'class': 'price'})
  price = price_box.text.strip()

  #save data in tuple
  data.append((name, price))

  import csv
  from datetime import datetime

  #open a csv file with append, so old data with not be erased
  with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for name, price in data:
      writer.writerow([name, price, datetime.now()])



