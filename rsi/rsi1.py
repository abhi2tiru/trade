import pandas as pd
import numpy as np

def matrix(days):
    tdays=503-days
    #getting company data
    tickers=pd.read_csv('C:\\Users\\abhin\\Desktop\\rsi\\tickers.csv')['tickers'].to_numpy()
    buy=np.zeros(tdays)
    sell=np.zeros(tdays)

    for i in range(954):

        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\'+tickers[i]+'.csv'
        data=pd.read_csv(path)

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
        rsi=data['rsi'].to_numpy()
        for j in range(tdays):
            if rsi[j]>70:
                sell[j]+=1
            if rsi[j]<30:
                buy[j]+=1
    return  pd.DataFrame({'buy':buy,'sell':sell}) 
