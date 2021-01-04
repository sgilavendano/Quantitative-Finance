import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web 

def get_adj_close(start, end, ticker):
  start = start
  end = end 
  info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
  return pd.DataFrame(info)

tesla = get_adj_close('1/1/2010','1/1/2020', 'tsla')

df['30 Day MA'] = pd.to_numeric(df['Adj Close'])
for item in (tesla):
    item['30 Day MA'] = item['Adj Close'].rolling(window=20).mean()
    
    item['30 Day STD'] = item['Adj Close'].rolling(window=20).std() 
    
    item['Upper Band'] = item['30 Day MA'] + (item['30 Day STD'] * 2)
    item['Lower Band'] = item['30 Day MA'] - (item['30 Day STD'] * 2)

