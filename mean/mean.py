import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


days=100
# read company file
data=pd.read_csv("C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\AAP.csv")
del data['otc']
# analyze data
data['time']=data['timestamp'].apply(lambda x:pd.to_datetime(x*1000000))
data['mean']=data['open'].rolling(days).mean()
# profit ratio
data['profit']=data['open'].shift(-1)
data['profit']=data['profit'].divide(data['open'])
# clean data
index=data.index
index=index[0:503-days]
data=data[days-1:-1]
money=10000
open=data['open'].to_numpy()
mean=data['mean'].to_numpy()
ratio=data['profit'].to_numpy()
profit=np.zeros(503-days)
#calculate profits
for i in range(503-days):
    if open[i]>mean[i]:
        profit[i]=(1-ratio[i])*money
    else:
        profit[i]=(ratio[i]-1)*money 

tstat=profit.mean()/profit.std()
#tstat
print(days)
print(tstat)
print(profit.sum())
plt.plot(index,profit.cumsum())
plt.show()