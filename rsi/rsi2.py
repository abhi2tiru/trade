import pandas as pd
import numpy as np
import plotly.express as px
from rsi1 import matrix

#getting comapany data
def rsi(days):
    tickers=pd.read_csv('C:\\Users\\abhin\\Desktop\\rsi\\tickers.csv')['tickers'].to_numpy()
    # getting no of bu sell companies on each trade day 

    tdays=503-days

    print('daily investment 1 million for rsi '+str(tdays)+'days')

    mat=matrix(days)
    buy=mat['buy'].to_numpy()
    sell=mat['sell'].to_numpy()
    profits=np.zeros(tdays)
    money=500000

    date=0
    for i in range(954):
        #read each comapny
        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\'+tickers[i]+'.csv'
        data=pd.read_csv(path)
        #calculating rsi
        data['next']=data['open'].shift(-1)
        data['diff']=data['open'].diff(1)
        buyfit=data['open'].diff(1)
        sells=data['open'].diff(1)
        buyfit[0]=0
        sells[0]=0
        buyfit[buyfit<0]=0
        sells[sells>0]=0
        data['next']=data['next']/data['open']
        data['buyfit']=buyfit.rolling(days).sum()
        data['sells']=abs(sells.rolling(days).sum())
        data['rs']=data['buyfit']/data['sells']
        data['rsi']=100 - 100/(data['rs']+1)
        data=data[days-1:-1]
        if i==953:
            data['timestamp']=data['timestamp'].apply(lambda x:pd.to_datetime(x*1000000))
            date=data['timestamp'].to_numpy()
        next=data['next'].to_numpy()
        rsi=data['rsi'].to_numpy()
        #adding profits to profits list 
        for j in range(tdays):
            if rsi[j]>70:
                profits[j]+=money*(1-next[j])/sell[j]
            if rsi[j]<30:
                profits[j]+= money*(next[j]-1)/buy[j]

    tstat=profits.mean()/profits.std()
    if tstat>0:
        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\AAPL.csv'
        data=pd.read_csv(path)
        data['date']=data['timestamp'].apply(lambda x:pd.to_datetime(x*1000000))
        date=data['date'].to_numpy()
        lamp=np.zeros(503)
        lamp[days-1:-1]=profits
        s='rsi_'+str(days)
        df=pd.DataFrame({'date':date,s:lamp})
        df.to_csv(s+'.csv')
    #calculting tstat   
    print('mean_days '+str( days))
    print('Total profits '+str(profits.sum()))
    print('tstat '+str(profits.mean()/profits.std()))    
    
    return profits.mean()/profits.std()
    fig=px.line(df,x="x",y="y",title="rsi profits")
    fig.show()