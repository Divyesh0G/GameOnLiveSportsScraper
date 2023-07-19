from bs4 import BeautifulSoup
import requests
import lxml
import datetime
import os
import math
import re

# Set the headers with a User-Agent to mimic a web browser
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

# Create an empty dictionary named 'data' to store the scraped data
data = {
    'NAME': [],
    'EMAIL': [],
}

# Specify the URL of the Game On Live Sports website
url = 'https://www.gameonlivesports.com.au/Find-Venues.aspx'

# Send a GET request to the URL using the requests library and store the response in the 'page' variable
page = requests.get(url,headers=headers)

# Create a BeautifulSoup object from the page content using the lxml parser
bs = BeautifulSoup(page.content,'lxml')

# Find the main container div element containing the venue information using its class
card = bs.find('div',class_='col-lg-12 col-sm-12').find('ul').findAll('li',style='display:')

# Iterate over each list item
for i in card:
    # Find the second anchor tag within the list item, which contains the venue name and its associated URL
    A_tag =  i.findAll('a')[1]
    name = A_tag.text
    ink = A_tag['href']
    
    # Send a GET request to the venue URL and store the response in the 'page_2' variable
    page_2 = requests.get(ink,headers=headers)
    bs2=BeautifulSoup(page_2.content,'lxml')
    
    # Find all the href elements within the page_2 content that contain ".com.au" in the URL
    for k in bs2.findAll(href=re.compile('.com.au')):
        print(k)
        print()
        print()
