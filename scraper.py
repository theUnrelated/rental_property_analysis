from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time 
import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import re
import random

start_time = time.time()
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
browser = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe', chrome_options=option)

# 4 main groups of data to be scraped
details = []
details2 = []
description = []
ammenities = []

i = 1 #page number

def scrape():
    while i < 102: # Page number which you want to scrape until
        time.sleep(random.randint(3,5))
        browser.get("###Insert URL to scrape###Insert page number as according to link###")
        WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.XPATH, "//div[@class='SearchListingItem__infoHeader__34JAu']")))
        i += 1 # next page
        link = []
        listing_link_element = browser.find_elements_by_xpath("//div[@class='SearchListingItem__infoHeader__34JAu']//a[@href]")
        print(i)
        for k in listing_link_element: # Getting link of all listings in a page
            l = k.get_attribute('href')
            link.append(l)

        for k in link: # Reading all listings of one page
            browser.get(k)
            WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.XPATH, "//div[@class='PhotoGallery__coverPhotoGalleryVideo__39AY9']")))
            listing_details_element = browser.find_elements_by_xpath("//div[@class='Listing__container__28Ee5']")
            listing_details = [x.text for x in listing_details_element]
            details.append([x.text for x in listing_details_element])

            listing_details2_element = browser.find_elements_by_xpath("//div[@class='Listing__keyDetailContainer__2Ky0e']")
            listing_details2 = [x.text for x in listing_details2_element]
            details2.append([x.text for x in listing_details2_element])  

            listing_ammenities_element = browser.find_elements_by_xpath("//div[@class='Listing__amenitiesContainer__2M8p3']")
            listing_ammenities = [x.text for x in listing_ammenities_element]
            ammenities.append([x.text for x in listing_ammenities_element])

            listing_description_element = browser.find_elements_by_xpath("//div[@class='Listing__section__2rvBa']")
            listing_description = [x.text for x in listing_description_element]
            description.append([x.text for x in listing_description_element])

            time.sleep(random.randint(1,3))

    print("--- %s seconds ---" % (time.time() - start_time))

scrape()

## Organizing scraped data and storing them

beds, address, tenure, price, size, ppst = [], [], [], [], [], []

for i in details:
    for k in i:
        k = re.sub('\n', ' ', k)
        if "View on map" in k:
            start = k.find('View on map') + 12
            end = start + 6
            output = k[start:end]
            beds.append(output.strip())
            
            start = k.find('Bed') + 4
            end = k.find('District')
            output = k[start:end]
            address.append(output)
            
            start = k.find('For rent') + 8
            output = k[start::]
            price.append(output)
        
            start = k.find('sqft') - 5
            end = start + 20
            output = k[start:end]
            if output[0] != "\d":
                size.append(output[1::])
            else:
                size.append(output)
            output2 = k[start+20:end+10]
            ppst.append(output2)
            
        if "Tenure" in k:
            start = k.find('Tenure') + 8
            output = k[start:start + 8]
            output = re.sub('- View m', 'Nan', output)
            tenure.append(output)
            
        elif "Key Details" in k:
            tenure.append('Nan')
            
furnishing, facing, pets, ethnic, lease = [], [], [], [], []
            
for i in details2:
    for k in i:
        k = re.sub('\n', ' ', k)
        if "Fully" in k:
            furnishing.append('Fully Furnished')
        elif "Partially" in k:
            furnishing.append('Partially Furnished')
        elif "Un" in k:
            furnishing.append("Unfurnished")
        else:
            furnishing.append('Nan')
            
        if "PETS" in k:
            start = k.find('PETS') + 5
            output = k[start:start + 12]
            pets.append(output)
        else:
            pets.append('Nan')
        if "FACING" in k:
            start = k.find('FACING') + 6
            output = k[start:start + 6]
            facing.append(output.strip())
        else:
            facing.append('Nan')
        if "LEASE" in k:
            start = k.find('LEASE') + 5
            output = k[start:start + 10]
            lease.append(output.strip())
        else:
            lease.append('Nan')
        if "ETHNIC" in k:
            start = k.find('ETHNIC') + 6
            output = k[start:start + 19]
            ethnic.append(output)
        else:
            ethnic.append('Nan')            

ammenity = []
for i in ammenities:
    if len(i) == 0 :
        i = ['Nan']
    for k in i:
        k = re.sub('\n', ' ', k)
        ammenity.append(k)

descrip, preference, p1, p2, p3, p4, p5, p6, p7 = [], [], [], [], [], [], [], [], [] 

for i in description:
    for k in i:
        if "Description" not in k:
            i.remove(k)            
    if len(i) == 0:
        i = ["Nan"]
    for k in i:
        k = re.sub('\n', '', k)
        k = re.sub('Description', '', k)
    descrip.append(k)
    for k in i:
        if "chinese" in k.lower():
            start = k.lower().find('chinese') - 30
            output = k[start:start + 80]
            p1.append(output)
        else:
            p1.append("Nan")
        if "prc" in k.lower():
            start = k.lower().find('prc') - 30
            output = k[start:start + 80]
            p2.append(output) 
        else:
            p2.append("Nan")
        if "filipino" in k.lower():
            start = k.lower().find('filipino') - 30
            output = k[start:start + 80]
            p3.append(output)
        else:
            p3.append("Nan")
        if "lady" in k.lower():
            start = k.lower().find('lady') - 30
            output = k[start:start + 80]
            p4.append(output)
        else:
            p4.append("Nan")
        if "malaysian" in k.lower():
            start = k.lower().find('malaysian')
            output = k[:start + 80]
            p5.append(output) 
        else:
            p5.append("Nan")
        if "female" in k.lower():
            start = k.lower().find('female') - 30
            output = k[start:start + 80]
            p6.append(output) 
        else:
            p6.append("Nan")
        if "indian" in k.lower():
            start = k.lower().find('indian') - 30
            output = k[start:start + 80]
            p7.append(output) 
        else:
            p7.append('Nan')

        

df = pd.DataFrame({"Address":address, "Beds":beds, "Size":size, "Price":price, "price/sqft":ppst, "Tenure":tenure,
                  "Furnishing":furnishing, "Pets":pets, "Lease": lease, "Ethnic": ethnic, 
                  "Ammenities":ammenity, "Description":descrip, 
                   "Chinese":p1, "PRC":p2, "Filipino":p3, "Lady":p4, "Malaysian":p5, "Female":p6, "Indians":p7})
                   
writer = ExcelWriter('data.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
