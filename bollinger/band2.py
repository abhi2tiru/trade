import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from band1 import matrix
#getting symbol list
tickers=pd.read_csv('C:\\Users\\abhin\\Desktop\\bollinger\\tickers.csv')['tickers'].to_numpy()
def band(days):
#getting no of buy and sell companies list  
    data=matrix(days)
    tdays=503-days
    print('Bollinger Bands daily investment 1 million for '+str(tdays)+'days')
    lap=data.index
    profit=data['buy'].to_numpy()
    loss=data['sell'].to_numpy()
    profits=np.zeros(tdays)
    money=500000
    for i in range(954):
        #getting each company
        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\'+tickers[i]+'.csv'
        data=pd.read_csv(path)
        #analyzing the company data
        data['mean']=data['open'].rolling(days).mean()
        data['std']=data['open'].rolling(days).std()
        data['gain']=data['open'].shift(-1)
        data['gain']=data['gain']/data['open']
        data['buy']=data['open']<(data['mean']-2*data['std'])
        data['sell']=data['open']>(data['mean']+2*data['std'])
        # cleaning the data
        data=data[days-1:-1]
        gain=data['gain'].to_numpy()
        buy=data['buy'].to_numpy()
        sell=data['sell'].to_numpy()
        # adding profits to profits list
        for j in range(tdays):
            if buy[j]:
                profits[j]+=money/profit[j]*(gain[j]-1)
            if sell[j]:
                profits[j]+=money/loss[j]*(1-gain[j])    
    tstat=profits.mean()/profits.std()
    if tstat>0:
        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\AAPL.csv'
        data=pd.read_csv(path)
        data['date']=data['timestamp'].apply(lambda x:pd.to_datetime(x*1000000))
        date=data['date'].to_numpy()
        lamp=np.zeros(503)
        lamp[days-1:-1]=profits
        s='band_'+str(days)
        df=pd.DataFrame({'date':date,s:lamp})
        df.to_csv(s+'.csv')
    #printing tstat
    print('mean_days '+str( days))
    print('Total profits '+str(profits.sum()))
    print('tstat '+str(profits.mean()/profits.std())) 
    return profits.mean()/profits.std()
    #plotting the graph
