import numpy as np 
import pandas as pd
data=pd.read_csv("C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\AAPL.csv")
del data['otc']
data['time']=data['timestamp'].apply(lambda x:pd.to_datetime(x*1000000))
data['mean']=data['open'].rolling(30).mean()
data['profit']=data['open'].shift(-1)
data['profit']=data['profit'].divide(data['open'])
data=data[29:-1]
data.at[29,'profit']=1
print(data)
