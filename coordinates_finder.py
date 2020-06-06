from nltk import word_tokenize
import numpy as np

import pandas as pd
df = pd.read_excel('data.xlsx')

#Initializing geopy APIs
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")

from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1, max_retries = 15, error_wait_seconds=10.0)

# Test run
address = 'Insert to test'
location = geolocator.geocode(address)
print(location.latitude, location.longitude)

# For the addresses scraped 
for i in range(0, df['Address'].count()):
    if str(df['Latitude'][i]) == 'nan'  or df['Latitude'][i] > 2.0:
        a = word_tokenize(df['Address'][i])
        for b in range(0, len(a)):
            location = geolocator.geocode(a[b]+' Singapore', timeout = 99)
        if location is None and (b+1 > len(a) == False):
            location = geolocator.geocode(a[b]+' '+a[b+1]+' Singapore', timeout = 99)
        elif location is None and (b+2 > len(a) == False):
            location = geolocator.geocode(a[b]+' '+a[b+1]+' '+a[b+2]+' Singapore', timeout = 99)
        elif location is None:
            location = geolocator.geocode(a[-b]+' Singapore', timeout = 99)
        elif location is None and (b+1 > len(a) == False):
            location = geolocator.geocode(a[-b]+' '+a[-b-1]+' Singapore', timeout = 99)
        elif location is None and (b+2 > len(a) == False):
            location = geolocator.geocode(a[-b]+' '+a[-b-1]+' '+a[-b-2]+' Singapore', timeout = 99)
    
        if location is not None:
            df['Latitude'][i] = location.latitude
            df['Longitude'][i] = location.longitude
            # print(a)
            
writer = pd.ExcelWriter('data_with_coords.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save( 
