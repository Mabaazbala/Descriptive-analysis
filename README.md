# Discriptive-analysis

### **Step 1: Import Libraries**
    from bs4 import BeautifulSoup
    import requests
    import sys
    import time
    import pandas as pd
    import urllib
    import csv

### Step 2: Scraping URL Link
    web_url='https://en.wikipedia.org/wiki/List_of_best-selling_mobile_phones'
    class_name = 'wikitable sortable'

### Step 3: Get Response
    response = requests.get(web_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)

### Step 4: FInd Attributes
    mobile_list = soup.find('table',attrs={'class':class_name })
    print(mobile_list)

### Step 5: Read the File
    data = pd.read_html(str(mobile_list))
    print(data)`

### Step 6:Select multiple columns
    select_table_column = ["Manufacturer","Model","Form factor","Smartphone?","Year","Graph (million units)","Graph (million units).1"]
    
    select_table_column
    Manufacturer = data[0][select_table_column]

### Step 7: Convert To CSV file
    Manufacturer
    Manufacturer.to_csv("mobilelist.csv",header=True)



