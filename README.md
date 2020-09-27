# Discriptive-analysis

from bs4 import BeautifulSoup
import requests
import sys
import time
import pandas as pd
import urllib
import csv

web_url ='https://en.wikipedia.org/wiki/List_of_best-selling_mobile_phones'
class_name = 'wikitable sortable'

response = requests.get(web_url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)

mobile_list = soup.find('table',attrs={'class':class_name })

print(mobile_list)

data = pd.read_html(str(mobile_list))

print(data)

##select multiple columns
select_table_column = ["Manufacturer","Model","Form factor","Smartphone?","Year","Graph (million units)","Graph (million units).1"]

select_table_column

Manufacturer = data[0][select_table_column]

Manufacturer

Manufacturer.to_csv("mobilelist.csv",header=True)
