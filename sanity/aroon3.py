import pandas as pd
import numpy as np
from aroon1 import matrix
import plotly.express as px
def aroon(days):
    tdays=503-days-1
    #read symbol list
    tickers=pd.read_csv('C:\\Users\\abhin\\Desktop\\trade\\arron\\tickers.csv')['tickers'].to_numpy()
    #initialize the profits list
    profits=np.zeros(tdays)
    # getting buy and sell companoes for each day
    data=matrix(days)
    buy=data['buy'].to_numpy()
    sell=data['sell'].to_numpy()
    #money spent on buying or selling
    print('daily investment 1 million for aroon '+str(tdays)+'days')
    money=500000
    #calculate the profits
    for i in range(954):
        #read each comapany
        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\'+tickers[i]+'.csv'
        data=pd.read_csv(path)
        open=data['open'].shift(-1).to_numpy()
        data['next']=data['open'].shift(-1)/data['open']
        data=data[days-1:-2]
        next=data['next'].to_numpy()
        for j in range(tdays):
            q=100*np.argmax(open[j:j+days])/days   
            w=100*np.argmin(open[j:j+days])/days
            if q>70 and w<30:
                profits[j]+=(money/sell[j])*(1-next[j])/-1
            if q<30 and w>70:
                profits[j]+=(money/buy[j])*(next[j]-1) /-1 
    tstat=profits.mean()/profits.std()
    if tstat>0:
        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\AAPL.csv'
        data=pd.read_csv(path)
        data['date']=data['timestamp'].apply(lambda x:pd.to_datetime(x*1000000))
        date=data['date'].to_numpy()
        lamp=np.zeros(503)
        lamp[days-1:-2]=profits
        s='aroon_'+str(days)
        df=pd.DataFrame({'date':date,s:lamp.cumsum()})
        df.to_csv(s+'od-1.csv')
        fig=px.line(df,x="date",y=s)
        fig.show()
    print('mean_days '+str( days))
    print('Total profits '+str(profits.sum()))
    print('tstat '+str(profits.mean()/profits.std()))    
    return profits.mean()/profits.std()
aroon(5)