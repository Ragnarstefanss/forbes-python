# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:26:06 2020

@author: Ragnar
"""
from pprint import pprint
import datetime
import time;
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

#columns
columns_main =  ['rank', 'name', 'net_worth', 'countryOfCitizenship', 'source', 'gender', 'financialAssets', 'estWorthPrev', 'privateAssetsWorth']
columns_financial_assets = ['financialAssets']

# ----------------------------------------------------------- #
## // Start: Assistant functions

def capitalize_first_letter_in_each_word(user_input):
    strList = user_input.split()
    new_string = ''
    for val in strList:
        new_string += val.capitalize()+ ' '
    return new_string.strip()


def search_by_name(df, call_type):
    while True:
        search_person = input("Enter persons name: ")
        new_name = capitalize_first_letter_in_each_word(search_person)
        df_to_search = (df[columns_main])
        match = df_to_search[df['name'].str.match(new_name)]
        try:
            if not match.empty:
                if(call_type == "search_billionaire"):
                    print(match)
                elif(call_type == "search_assets"):
                    print(match[columns_financial_assets])
                print("Do you want to save " + new_name + " assets to html file")
                search_person = input("< yes | no >: ")
                if(search_person == 'y' or search_person == 'yes'):
                    pprint(match[columns_financial_assets])
                    #match[columns_financial_assets].to_html(new_name + '_assets.html')
                else:
                    print("no html file created")
                break
            else:
                print("No person by that name")
                continue
        except ValueError:
            print ("call_assets_persons_name ValueError")
            continue 
## // End: Assistant functions
# ----------------------------------------------------------- #
    
## // Start: call functions
def call_search_billionaire(df):
    search_by_name(df, "search_billionaire")

def call_search_billions(df):
    #TODO: error check for input 'not int'
   billions_value = input("Enter amount in billions: ")
   search_billions(df, billions_value)
   
def call_assets_person_name(df):
    search_by_name(df, "search_assets") 

def call_search_country(df):
    return 0

def call_create_plot(df):
    #hist, scatter, etc..
    age_list = []
    for index, row in df.iterrows():
        today = date.today() 
        birthDate = (row['birthDate'] / 1000)
        datetime_birthDate = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=(birthDate))
        age = today.year - datetime_birthDate.year - ((today.month, today.day) < (datetime_birthDate.month, datetime_birthDate.day)) 
        age_list.append(age)
    df['age'] = age_list
    df.plot(x="age", y="net_worth", kind="scatter")
    plt.show()

## // End: call functions
# ----------------------------------------------------------- #
    
## // START: Main function

# 2. More than <value> Billions + -> search_billions(<value>)
def search_billions(df, value):
    new_value = int(value) * 1000
    print(df[df['net_worth'] > new_value][columns_main])

## // END: Main function