#!/usr/bin/env python
# coding: utf-8

# In[54]:


##    Problem: We are asked to provide a code that gets the currency rate for given date in python

##    We'll use Open Exchange Rates, https://docs.openexchangerates.org/ , because it provides a simple, 
# lightweight and portable JSON API with live and historical foreign exchange (forex) rates, via a simple and 
# easy-to-integrate API, in JSON format. Data are tracked and blended algorithmically from multiple reliable sources, 
# ensuring fair and unbiased consistency.

##    https://openexchangerates.org/ offers a free version, with some limits
# and add the information about the amounts in local currency to the data set.
 
##    Authentication: app_id=c92e9bfec2584ff0848965f86681ec37


# In[61]:


# In order to make it easier for end users, we will use input
print("Please enter the input date in YYYY-MM-DD format:")
a = input()
b = 'https://openexchangerates.org/api/historical/' + a + '.json?app_id=c92e9bfec2584ff0848965f86681ec37'
# First part refers to api's website to use api, a refers to required date, Last part refers to app authentication


# In[62]:


# Sending HTTP request
import requests 
# Working with DataFrames in pandas
import pandas as pd
# Importing date 
from datetime import datetime

rsp = requests.get(b).json()
 
rsp


# In[63]:


#lets convert above definition into DataFrame, and add two new columns for currency date and imported date

df = pd.DataFrame(rsp['rates'].items(), columns=['currency_name', 'currency_rate'])
df['curreny_date'] = datetime.fromtimestamp(rsp['timestamp'])
df['imported_date'] = pd.to_datetime('now')
pd.set_option('display.max_rows',None)
df


# In[65]:


# If you want to see only one of the currency:
print('Please write the abbreviation of required currency:')
c = input()
df[df['currency_name']==c]


# In[ ]:




