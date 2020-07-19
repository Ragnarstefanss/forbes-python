"""
Working with fortbes billionaires list data
"""

import numpy as np
import pandas as pd
import urllib.request, json 
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',25)

with urllib.request.urlopen("https://forbes400.herokuapp.com/api/forbes400?limit=10") as url:
    data = json.loads(url.read().decode())

df = pd.json_normalize(data)
df.drop(['name'], axis=1, inplace=True)

df.rename(columns = {'personName':'name'}, inplace=True)
df.rename(columns = {'finalWorth':'net_worth'}, inplace=True)
print(df.info())
columns_main =  ['rank', 'name', 'net_worth', 'countryOfCitizenship', 'source', 'gender', 'financialAssets', 'estWorthPrev', 'privateAssetsWorth']
print (df[columns_main])


#print("Search by \n",
 #     "1. Billions -> search_billions(<value>) \n",
 #     "2. Country -> seach_country(<country name>) \n"
 #     "3. Gender -> search_gender(< m | f > \n"
 #     "4. Persons Assets -> assets(<persons name>, :number_of_shares)"
 #     "\n"
 #     " <> = replace with value, \n"
 #     " : = optinal argument \n "
#)

#def search_billions(n):
    