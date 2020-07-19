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
#print(df.info())
columns_main =  ['rank', 'name', 'net_worth', 'countryOfCitizenship', 'source', 'gender', 'financialAssets', 'estWorthPrev', 'privateAssetsWorth']
#print (df[columns_main])

## // Start: Assistant functions

def capitalize_first_letter_in_each_word(user_input):
    strList = user_input.split()
    new_string = ''
    for val in strList:
        new_string += val.capitalize()+ ' '
    return new_string.strip()

## // End: Assistant functions

## // Start: Main Functions

def call_search_billions():
   billions_value = input("Enter amount in billions: ")
   search_billions(billions_value)
   
def call_assets_person_name():
    while True:
        assets_persons_name = input("Enter persons name: ")
        new_name = capitalize_first_letter_in_each_word(assets_persons_name)
        df_to_search = df[:].fillna('')
        df_to_search2 = (df_to_search[columns_main])
        match = df_to_search2[df_to_search2['name'].str.match(new_name)]
        try:
            if not match.empty:
                print(match)
                break
            else:
                print("No person by that name")
                
                continue
        except ValueError:
            print ("call_assets_persons_name ValueError")
            continue   
# Options menu
def options(): 
    while True:
        max_value = 5
        print("\n Search by \n",
              "\n",
              "1. More than <value> Billions -> search_billions(<value>) \n",
              "2. Country -> search_country(<country name>) \n"
              "3. Gender -> search_gender(< m | f > \n"
              "4. Persons Assets -> assets(<persons name>, :number_of_shares)\n"
              "5. QUIT"
        )
        
        user_input = int(input("Enter a number: "))
        try:
            #if(int(user_input) <= 0 or int(user_input) > max_value):
                #print ('Enter a valid number')
                #continue
            if user_input == 1:
                call_search_billions()
            if user_input == 2:
                continue
            if user_input == 3:
                continue
            if user_input == 4:
                call_assets_person_name()
            elif user_input == 5:
                break
        except ValueError:
            print ('Enter a valid number')
            continue
        
# 1 More than <value> Billions + -> search_billions(<value>)
def search_billions(value):
    new_value = int(value) * 1000
    print(df[df['net_worth'] > new_value][columns_main])

## // END: functions

# call options menu    
options()
    