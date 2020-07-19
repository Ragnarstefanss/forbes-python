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
from functions import *

with urllib.request.urlopen("https://forbes400.herokuapp.com/api/forbes400?limit=10") as url:
    data = json.loads(url.read().decode())

df = pd.json_normalize(data)
df.drop(['name'], axis=1, inplace=True)

df.rename(columns = {'personName':'name'}, inplace=True)
df.rename(columns = {'finalWorth':'net_worth'}, inplace=True)
#print(df.info())

#print (df[columns_main])


    
    
# Options menu
def options(): 
    while True:
        max_value = 6
        print("\n Search by \n",
              "\n",
              "1. Search billionaire by name -> search_billionaire(<persons name>) \n"
              "2. More than <value> Billions -> search_billions(<value>) \n",
              "3. Country -> search_country(<country name>) \n"
              "4. Gender -> search_gender(< m | f > \n"
              "5. Persons Assets -> assets(<persons name>, :number_of_shares)\n"
              "6. QUIT"
        )
        
        user_input = int(input("Enter a number: "))
        try:
            if(int(user_input) <= 0 or int(user_input) > max_value):
                print ('Enter a valid number')
                continue
            if user_input == 1:
                call_search_billionaire(df)
            if user_input == 2:
                call_search_billions(df)
            if user_input == 3:
                call_search_country(df)
                continue
            if user_input == 4:
                continue
            if user_input == 5:
                call_assets_person_name(df)
            elif user_input == 6:
                break
        except ValueError:
            print ('Enter a valid number')
            continue
        

## // END: Main functions

# call options menu    
options()
    