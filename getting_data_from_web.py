from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
import time
import requests

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

#configure web driver, not needed when using requests
def configure_driver_chrome(chrome_driver_path, link):
    driver = webdriver.Chrome(chrome_driver_path_isabela)
    driver.get(link)

    return driver


#functions
def reading_soup_contents_panadew():
    #seeting variables
    house = []
    prices = []
    bedrooms_and_availability = [] 
    bedrooms = []
    availability = []
    info = []
    links = []
    count = 0

    #getting the acutal content, using requests and html parser
    r = requests.get(panadew)
    soup = BeautifulSoup(r.content, 'html.parser')
    # attempt using driver, requests is quicker
    #content = driver.page_source
    #soup = BeautifulSoup(content, features="html.parser")

    #finding all available listings using soup
    for a in soup.findAll("div", {"class" : "four columns listingblockgrid listingblock"}):
        name = a.find('h4', attrs={'class':"address"})
        price = a.find('p', attrs={'class':'price'})
        bedrooms_and_availability = a.find('p', attrs={'class':'twofeatures'})
        #finding all the links
        for l in a.findAll('a', {"class": "btn btn-lightgray"}):
            try:
                links.append(l['href'])
                
            except KeyError:
                pass
        
        #appending found info
        house.append((name.text).strip("\n\t"))
        prices.append((price.text).strip("\n\t"))
        bedrooms_and_availability.strip("\n\t")
        bedrooms.strip("|")
        print(bedrooms)
        #bedrooms.append((bedroom_info.text).strip("\n\t"))
        
        

   
    
    #df = pd.DataFrame({'House':house,'Price':prices,'bedrooms':bedrooms, 'links':links}) 
    
    #df.to_csv('panadew.csv', index=False)




####################### main 

#d = configure_driver_chrome(chrome_driver_path_isabela, panadew)
reading_soup_contents_panadew()



