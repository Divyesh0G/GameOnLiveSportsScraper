from bs4 import BeautifulSoup
import requests
import lxml
# import pandas as pd
import datetime
import os
import math
import re

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
data = {
	'NAME': [],
	'EMAIL': [],
}

url = 'https://www.gameonlivesports.com.au/Find-Venues.aspx'

page = requests.get(url,headers=headers)



bs = BeautifulSoup(page.content,'lxml')


    

card = bs.find('div',class_='col-lg-12 col-sm-12').find('ul').findAll('li',style='display:')

for i in card:
    A_tag =  i.findAll('a')[1]
    name = A_tag.text
    ink = A_tag['href']
    page_2 = requests.get(ink,headers=headers)
    bs2=BeautifulSoup(page_2.content,'lxml')
    for k in bs2.findAll(href=re.compile('.com.au')):
        print(k)
        print()
        print()
        # print(k.string)
        # print()
    # try:
    	# mail = bs2.find('a',class_='sqs-svg-icon--wrapper email')['href']
    # except:
        # mail = 'Not ther'
    # print(f'>{len(card)}<>{name}<>{mail}<<')
