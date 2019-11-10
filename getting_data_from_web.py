from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
import time

chrome_driver_path_isabela = "C:\\Users\\isabe\\Downloads\\chromedriver_win32\\chromedriver.exe"
# websites 
panadew = "https://www.panadew.ca/search-results/?lang=#headeranchor"
frontenac = "https://www.frontenacproperty.com/properties/student/?bedrooms=1&sort=availability&order=ASC"
bpe = "https://bpe-rentals.com/?s=&property_status=&property_type=&property_location=Kingston&min_price=&max_price=&min_bedrooms=1&max_bedrooms=2&min_bathrooms=&max_bathrooms=&min_area=&max_area=&min_parking_place=&max_parking_place=&post_type=tm-property" 
highpoint = "https://highpointproperties.ca/unit-search/?city=Kingston&type=1&price&prox&available=-1&submit=submit" 
keyprop = "http://www.keyprop.com/listings/"
queens_housing_listings = "https://listingservice.housing.queensu.ca/index.php/rental/rentalsearch/action/results_list/"
heron = "https://www.heronmanagement.com/listings/" 
axon = "https://axonproperties.ca/available-rentals/" 



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

d = configure_driver_chrome(chrome_driver_path_isabela, frontenac)
reading_soup_contents(d)



