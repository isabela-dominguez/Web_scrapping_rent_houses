from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
import time

chrome_driver_path_isabela = "C:\\Users\\isabe\\Downloads\\chromedriver_win32\\chromedriver.exe"
panadew = "https://www.panadew.ca/search-results/?lang=#headeranchor"
frontenac = "https://www.frontenacproperty.com/properties/student/?bedrooms=1&sort=availability&order=ASC"
# Frontenac's robots.txt file: 
# User-agent: *
# Disallow: /wp-admin/
# Allow: /wp-admin/admin-ajax.php
# Disallow: /author/

#configure web driver 
def configure_driver_chrome(chrome_driver_path, link):
    driver = webdriver.Chrome(chrome_driver_path_isabela)
    driver.get(link)

    return driver


def reading_soup_contents(driver):
    #seeting variables
    house = []
    price = []
    availability = [] 

    #getting the acutal content
    content = driver.page_source
    soup = BeautifulSoup(content)

    for a in soup.findAll('a'):
        print("################# soup content")
        #print(a)
        print(soup.get_text())
        #name = a.find('div', attrs={'class':"row property-listings grid"})
        #price = a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        #rating = a.find('div', attrs={'class':'hGSR34 _2beYZw'})

        #house.append(name.text)
        #prices.append(price.text)
        #ratings.append(rating.text) 

    print(house)



####################### main 

d = configure_driver_chrome(chrome_driver_path_isabela, panadew)
reading_soup_contents(d)



