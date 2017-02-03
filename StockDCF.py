# The goal of this program is to pull stock 10K / 10Q info and store in Excel
# in a format that is useful to perform a DCF analysis.

import re
import urllib.request
from bs4 import BeautifulSoup


# Get URL and create da soup
html = urllib.request.urlopen('https://www.bloomberg.com/quote/TWTR:US')
soup = BeautifulSoup(html, "html.parser")

# Initialize list of hard to grab div values
classList = ['52Wk Range', 'Previous Close']

# Print easy to grab div classes 
print(soup.title.text)
price = soup.findAll('div', attrs={'class':'price'})
ticker = soup.findAll('div', attrs={'class':'ticker'})
dateTime = soup.findAll('div', attrs={'class':'price-datetime'})

# Create list to house stock values we want
stockList = []

# Convert from BS4 resultSet object to string and store in list
for x in ticker:
    stockList.append(str(x))

for x in price:
    stockList.append(str(x))

for x in dateTime:
    stockList.append(str(x))

# Strip div tags
for index in range(len(stockList)):
    stockList[index] = re.sub('<.*?>', '', stockList[index])

print(stockList, sep='\n')

#for x in range(0,2):
    #classString = classList[x]
    #print(soup.find('div', attrs={'class':classString}))
    #x = x + 1
    
