import pandas as pd
import numpy as np
#get Symbol list
def matrix(days):
    tdays=503-days
    tickers=pd.read_csv('C:\\Users\\abhin\\Desktop\\trade\\mean\\tickers.csv')['tickers'].to_numpy()
    #create matrix to store buy sell for each day
    result=np.zeros((954,tdays))
    for i  in range(954):
        #read each comapany
        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\'+tickers[i]+'.csv'
        data=pd.read_csv(path)
        data['mean']=data['open'].rolling(days).mean()
        data=data[days-1:-1]
        data['action']=data['open']<data['mean']
        action=data['action'].to_numpy()
        # set buy sell for each day
        for j in range(tdays):
            if action[j]:
                result[i][j]=1
            else:
                result[i][j]=-1

    lar=pd.DataFrame(result)
    ratios=np.zeros(tdays)
    for i in range(tdays):
        sum=lar[i].sum()
        ratios[i]=(sum+954)/2
    #get no of buy comapanies    
    
    return ratios






