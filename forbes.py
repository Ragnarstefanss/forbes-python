"""
Working with fortbes billionaires list data
"""

import numpy as np
import pandas as pd
import urllib.request, json 
import pandas as pd 

with urllib.request.urlopen("https://forbes400.herokuapp.com/api/forbes400?limit=10") as url:
    data = json.loads(url.read().decode())
    #print(json.dumps(data, indent=4))

df = pd.json_normalize(data)
print(df.info())
#print(df['personName'] + ' rank ' +  str(df['rank']) + ' net worth ' + str(df['finalWorth']))
