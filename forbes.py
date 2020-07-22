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
url = "https://forbes400.herokuapp.com/api/forbes400?limit=150"

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

df_json = pd.json_normalize(data)
#this was always set to the same value which was irrelevant so it got dropped
df_json.drop(['name'], axis=1, inplace=True)

df_json.rename(columns = {'personName':'name'}, inplace=True)
df_json.rename(columns = {'finalWorth':'net_worth'}, inplace=True)
df = df_json[:]

#Fill in nan values
df['bio'] = df['state'].fillna('no bio')
df['state'] = df['state'].fillna('unknown')
df['city'] = df['city'].fillna('unknown')
df['gender'] = df['gender'].fillna('unknown')
df['birthDate'] = df['birthDate'].fillna(0)
#df['financialAssets']
#df['shortUri']
#df['listShortUri']
#df['privateAssetsWorth']
#df['archivedWorth']
#df['thumbnail']
#df['squareImage']
#df['bios']
#df['abouts']
#df['person.squareImage ']

#print(df.isnull().sum()) 
print(df.info())


def valid_user_input(number, max_value):
    if(int(number) <= 0 or int(number) > max_value):
        print ('Enter a valid number')
        return False
    else:
        return True
        

def search_options():
    while True:
        print("\n Search billionaires by \n",
              "1. Name\n",
              "2. Gender\n"
              "3. Networth more than <value> billions\n",
              "4. Country citicenship\n",
              "5. EXIT (Go back to main menu)\n"
        )
        max_value = 5
        user_input = int(input("Enter a number: "))
        try:
            if(valid_user_input(user_input, max_value) != True):
                continue
            if user_input == 1:
                #1. Name
                call_search_billionaire(df)
            if user_input == 2:
                #2. Gender
                continue
            if user_input == 3:
                #3. Net worh over <X> billions
                call_search_billions(df)
            if user_input == 4:
                #4. Contry
                call_search_country(df)
            elif user_input == max_value:
                break
        except ValueError:
            print ('Enter a valid number')
            continue

# Options menu
def main_options(): 
    while True:
        print("1. Search billionaires\n",
              "2. Show billionaires investment assets\n",
              "3. Create graphs\n",
              "4. Quit\n",
        )
        max_value = 4
        user_input = int(input("Enter a number: "))
        try:
            if(valid_user_input(user_input, max_value) != True):
                continue
            if user_input == 1:
                #1. Search billionaires -> menu for search
                search_options()
            if user_input == 2:
                #2. Investment assets
                call_assets_person_name(df)
            if user_input == 3:
                #3. Create plots
                call_create_plot(df)
            elif user_input == max_value:
                break
        except ValueError:
            print ('Enter a valid number')
            continue
        

## // END: Main functions

# call options menu    
main_options()
    