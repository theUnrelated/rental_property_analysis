import pandas as pd
import googlemaps
import numpy as np
from tqdm.notebook import tqdm

df = pd.read_excel('data_with_coords_dist.xlsx')
df.head()

# Generating list of keywords to pick out in description of each rental listing
keywords = ['chinese couple', 'chinese lady', 'chinese landlord', 'chinese family', 'chinese man', 'chinese male',
            'chinese female', 'chinese owner', 'chinese mother', 'chinese father', 'chinese parents', 'chinese house',
            'staying with', 'no landlord', 'no owner']
for i in keywords:
    if "chinese" in i:
        a = i.split()
        keywords.append('malay ' + a[1])
        keywords.append('indian ' + a[1])

result, count = [], 0
for i in tqdm(range(0, len(df))):
    for k in keywords:
        try: 
            if k in df.iat[i, 16].lower():
                a.append(i)
                a.append(k)
                count += 1
        except:
            continue
            
  print(count)
  print(result) 
