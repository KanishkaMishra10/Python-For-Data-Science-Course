#!/usr/bin/env python
# coding: utf-8

# # CoinGecko is a cyrptocurrency API

# In[1]:


get_ipython().system('pip install pycoingecko')
get_ipython().system('pip install plotly')
get_ipython().system('pip install mplfinance')


# In[3]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc


# # This part first gets the movements of the price of a currency and then displays a candlestick graph which indicates the minimum value, starting value, closing value, and highest value of bitcoin on a particular day.

# In[4]:


cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

type(bitcoin_data)


# In[5]:


bitcoin_price_data = bitcoin_data['prices']        #selecting the prices

bitcoin_price_data[0:5]


# In[6]:


data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])      #creating a dataframe with 2 columns named TimeStamp and Price
data


# In[7]:


data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))      #converting the TimeStamp to data-time and saving it in a new column for human readablility and understanding
data


# In[8]:


candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})        #grouping the data by the 'Date' and finding the min, max, first and last
candlestick_data


# In[9]:


fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])    
                ])                                         #creating a candlestick chart

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()


