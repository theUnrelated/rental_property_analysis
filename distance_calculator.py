import pandas as pd
import googlemaps
import numpy as np
from tqdm.notebooks import tqdm
from geopy import distance

# Initializing googlemaps API
gmaps_key = googlemaps.Client(key="##Opps, use your own api key##")

# Initializing data 
df = pd.read_excel('data_with_coordinates.xlsx')
df.head()

df['Nearest mrt'] = None
df['Distance_mrt(km)'] = None
df['Nearest sch'] = None
df['Distance_sch(km)'] = None
df['Nearest mall'] = None
df['Distance_mall(km)'] = None
df['Nearest cbd'] = None
df['Distance_cbd(km)'] = None
df['Nearest uni'] = None
df['Distance_uni(km)'] = None

df.columns # To see total columns and for the next part of the code. AGAIN.. I probably should have used loc instead.

# Additional step I had to take to ensure the next step runs as I realised some coordinates returned are wrong e.g they were in other countries
for i in tqdm(range(0, len(df))):
    if df.iat[i, 26] > 2.0 or df.iat[i, 26] < 0.0 or str(df.iat[i, 26]) == 'nan':
        try:
            geocode_result = gmaps_key.geocode('Singapore {}'.format(df.iat[i,2]))
            lat = geocode_result[0]['geometry']['location']['lat']
            lon = geocode_result[0]['geometry']['location']['lng']
            df.iat[i, 25] = lon
            df.iat[i, 26] = lat
        except:
            lat, lon = None, None
        
# Now for the finale 
def calculate_distance_to_ammenities():
  for i in tqdm(range(0, len(df))):
      d = 100.0
      a = (df.iat[i,26], df.iat[i,25])
      for k in range(0, len(mrt)):
          b = (mrt.iat[k,1], mrt.iat[k,2])
          c = distance.distance(a, b).km
          if c < d:
              df.iat[i, 35] = mrt.iat[k, 0]
              df.iat[i, 36] = c
              d = c

  for i in tqdm(range(0, len(df))):
      d = 100.0
      a = (df.iat[i,26], df.iat[i,25])
      for k in range(0, len(sch)):
          b = (sch.iat[k,2], sch.iat[k,3])
          c = distance.distance(a, b).km
          if c < d:
              df.iat[i, 37] = sch.iat[k, 1]
              df.iat[i, 38] = c
              d = c

  for i in tqdm(range(0, len(df))):
      d = 100.0
      a = (df.iat[i,26], df.iat[i,25])
      for k in range(0, len(mall)):
          b = (mall.iat[k,1], mall.iat[k,2])
          c = distance.distance(a, b).km
          if c < d:
              df.iat[i, 39] = mall.iat[k, 0]
              df.iat[i, 40] = c
              d = c

  for i in tqdm(range(0, len(df))):
      d = 100.0
      a = (df.iat[i,26], df.iat[i,25])
      for k in range(0, len(cbd)):
          b = (cbd.iat[k,1], cbd.iat[k,2])
          c = distance.distance(a, b).km
          if c < d:
              df.iat[i, 41] = cbd.iat[k, 0]
              df.iat[i, 42] = c
              d = c

  for i in tqdm(range(0, len(df))):
      d = 100.0
      a = (df.iat[i,26], df.iat[i,25])
      for k in range(0, len(uni)):
          b = (uni.iat[k,1], uni.iat[k,2])
          c = distance.distance(a, b).km
          if c < d:
              df.iat[i, 43] = uni.iat[k, 0]
              df.iat[i, 44] = c
              d = c
              
 calculate_distance_to_ammenities()
 
writer = pd.ExcelWriter('data_with_coords_dist.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()
