import pandas as pd
import numpy as np

days=40
tdays=503-days
#getting company data
data=pd.read_csv('AAPL.csv')
#data analysis
data['next']=data['open'].shift(-1)
#getting today day - yesterday price  
data['diff']=data['open'].diff(1)
# getting only positive price differences
profit=data['open'].diff(1)
# getting only negative price differences
loss=data['open'].diff(1)
profit[0]=0
loss[0]=0
profit[profit<0]=0
loss[loss>0]=0

# aggregating the ups and downs
data['profit']=profit.rolling(days).sum()
data['loss']=abs(loss.rolling(days).sum())

#calculating rs and rsi 
data['rs']=data['profit']/data['loss']
data['rsi']=100 - 100/(data['rs']+1)
data=data[days-1:-1]
print(data)
print(len(data))