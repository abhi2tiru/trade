import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mean1 import matrix

def mean(days):
    tdays=503-days
    print('daily investment 1 million for mean reversion'+str(tdays)+'days')

    #create profits list
    profits=np.zeros(tdays)
    #get Symbol list
    tickers=pd.read_csv('C:\\Users\\abhin\\Desktop\\mean\\tickers.csv')['tickers'].to_numpy()
    #read no of buy companies in each day
    ratios=matrix(days)
    money=500000
    for i in tickers:
        # read each company
        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\'+i+'.csv'
        data=pd.read_csv(path)
        data['mean']=data['open'].rolling(days).mean()
        data['profit']=data['open'].shift(-1)/data['open']
        data['action']=data['open']<data['mean']
        data=data[days-1:-1]
        action=data['action'].to_numpy()
        profit=data['profit'].to_numpy()
        #calculate profit for each day
        for j in range(tdays):
            if action[j]:
                profits[j]+=money*(profit[j]-1)/ratios[j]
            else:
                profits[j]+=money*(1-profit[j])/(954-ratios[j])
    print('mean_days '+str( days))
    print('Total profits '+str(profits.sum()))
    print('tstat '+str(profits.mean()/profits.std()))    
    index=np.zeros(tdays)
    for i in range(tdays):
        index[i]=i
    tstat=profits.mean()/profits.std()
    if tstat>0:
        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\AAPL.csv'
        data=pd.read_csv(path)
        data['date']=data['timestamp'].apply(lambda x:pd.to_datetime(x*1000000))
        date=data['date'].to_numpy()
        lamp=np.zeros(503)
        lamp[days-1:-1]=profits
        s='mean_'+str(days)
        df=pd.DataFrame({'date':date,s:lamp})
        df.to_csv(s+'.csv')
    return profits.mean()/profits.std()   
    plt.plot(index,profits.cumsum())
    plt.show()