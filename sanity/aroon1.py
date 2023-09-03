import pandas as pd
import numpy as np

def matrix(days):
    tdays=503-days-1
    #read symbol list
    tickers=pd.read_csv('C:\\Users\\abhin\\Desktop\\trade\\arron\\tickers.csv')['tickers'].to_numpy()
    
    #initilize two arrays for aroon up and  aroon down
    up =np.zeros(tdays)
    down=np.zeros(tdays)
    # initialize buy and sell liststo store no of companies for each day            
    buy=np.zeros(tdays)
    sell=np.zeros(tdays)
    for i  in range(954):
        #read each comapany
        path='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\'+tickers[i]+'.csv'
        data=pd.read_csv(path)

        open=data['open'].shift(-1).to_numpy()
        for j in range(tdays):
            up[j]=100*np.argmax(open[j:j+days])/days   
            down[j]=100*np.argmin(open[j:j+days])/days
            q=up[j]
            w=down[j]
            if q>70 and w<30:
                sell[j]+=1
            if q<30 and w>70:
                buy[j]+=1                     
                
    # saving buy sell list 
    return pd.DataFrame({'buy':buy,'sell':sell})
