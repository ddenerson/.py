import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/aapl'
page = requests.get(url)
page.text
soup = BeautifulSoup(page.text,'lxml')

# webscraper Stock marketwatch 

#1. get the current price of the stock
bigger_stock_price = soup.find_all('bg-quote' , class_ = 'value')[0].text
print("Main stock price:",bigger_stock_price)
# get closing price of stock
previous_close = soup.find_all('td' , class_ = 'table__cell u-semi')[0].text
print("Previous close:",previous_close)
print("----------------------------------------")
# 52 week range (lower, upper)
week_range = soup.find_all('div' , class_ = 'range__header')[2].text
print(week_range)
print("----------------------------------------")

#5. analyst rating
analyst_ratings = soup.find_all('li' , class_ = 'analyst__option active')[0].text
print("Analyst rating:",analyst_ratings)
