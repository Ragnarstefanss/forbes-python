"""
Working with fortbes billionaires list data
"""

import numpy as np
import pandas as pd
import urllib.request, json 
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')
from pprint import pprint
pd.options.display.max_columns = None
from functions import *
import datetime

# Program still in DEV mode so I want to quickly be able to change url without losing old url
#url = "https://forbes400.herokuapp.com/api/forbes400"
url = "https://forbes400.herokuapp.com/api/forbes400?limit=10"

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

df_json = pd.json_normalize(data)
df_json.drop(['name'], axis=1, inplace=True)

df_json.rename(columns = {'personName':'name'}, inplace=True)
df_json.rename(columns = {'finalWorth':'net_worth'}, inplace=True)
df = df_json[:].fillna('')
#print(df.info())

# Options menu
def options(): 
    while True:
        
        print("\n Search by \n",
              "\n",
              "1. Search billionaire by name -> search_billionaire(<persons name>) \n"
              "2. More than <value> Billions -> search_billions(<value>) \n",
              "3. Country -> search_country(<country name>) \n"
              "4. Gender -> search_gender(< m | f > \n"
              "5. Persons Assets -> assets(<persons name>, :number_of_shares)\n"
              "6. Create a histogram\n"
              "7. QUIT"
        )
        max_value = 7
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
            if user_input == 6:
                call_create_plot(df)
            elif user_input == 7:
                break
        except ValueError:
            print ('Enter a valid number')
            continue
        

## // END: Main functions

# call options menu    
options()
    