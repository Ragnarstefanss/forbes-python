# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:26:06 2020

@author: Ragnar
"""

columns_main =  ['rank', 'name', 'net_worth', 'countryOfCitizenship', 'source', 'gender', 'financialAssets', 'estWorthPrev', 'privateAssetsWorth']

## // Start: Assistant functions

def capitalize_first_letter_in_each_word(user_input):
    strList = user_input.split()
    new_string = ''
    for val in strList:
        new_string += val.capitalize()+ ' '
    return new_string.strip()

## // End: Assistant functions
    


## // Start: call functions
def call_search_billionaire(df):
    while True:
        search_person = input("Enter persons name: ")
        new_name = capitalize_first_letter_in_each_word(search_person)
        df_to_search2 = (df[columns_main])
        match = df_to_search2[df['name'].str.match(new_name)]
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

def call_search_billions(df):
   billions_value = input("Enter amount in billions: ")
   search_billions(df, billions_value)
   
def call_assets_person_name(df):
    while True:
        assets_persons_name = input("Enter persons name: ")
        new_name = capitalize_first_letter_in_each_word(assets_persons_name)
        df_to_search2 = (df[columns_main])
        match = df_to_search2[df['name'].str.match(new_name)]
        try:
            if not match.empty:
                print(df_to_search2[['financialAssets']])
                break
            else:
                print("No person by that name")
                
                continue
        except ValueError:
            print ("call_assets_persons_name ValueError")
            continue   

def call_search_country(df):
    return 0

## // End: call functions

## START: Main function

# 2. More than <value> Billions + -> search_billions(<value>)
def search_billions(df, value):
    new_value = int(value) * 1000
    print(df[df['net_worth'] > new_value][columns_main])

## END: Main function