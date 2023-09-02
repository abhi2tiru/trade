import pandas as pd 
import numpy as np

def matrix(days):
    tdays=503-days
    # read the company names
    tickers=pd.read_csv('C:\\Users\\abhin\\Desktop\\bollinger\\tickers.csv')['tickers'].to_numpy()
    # create a matrix with no of companies and real trading days 
    result=np.zeros((954,tdays))
    #calculating how much to invest in each day for buying and selling
    for i in range(954):
        # read each company
        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\'+tickers[i]+'.csv'
        data=pd.read_csv(path)
        data['mean']=data['close'].rolling(days).mean()
        data['std']=data['close'].rolling(days).std()
        data['pro']=data['mean']+2*data['std']
        data['loss']=data['mean']-2*data['std']
        data['buy']=data['close']<data['loss']
        data['sell']=data['close']>data['pro']
        data=data[days-1:-1]
        buy=data['buy'].to_numpy()
        sell=data['sell'].to_numpy()
        for j in range(tdays):
            if buy[j]:
                result[i][j]=1
            if sell[j]:
                result[i][j]=-1
    data=pd.DataFrame(result)
    profit=np.zeros(tdays)
    loss=np.zeros(tdays)
    #calculating no of buy and sell companies
    for i in range(tdays):
        temp=data[i].to_numpy()
        q=0
        w=0
        for j in temp:
            if j==1:
                q+=1
            if j==-1:
                w+=1    
        profit[i]=q
        loss[i]=w
    data=pd.DataFrame({'buy':profit,'sell':loss})
    #saving no of buy sell companies in each trade day
    return data    
