import pandas as pd 
import numpy as np

arr=np.zeros((0,473),dtype=np.int16)
data=pd.DataFrame(arr)
n1=np.ones(473)
data.loc[0]=n1
def ka(x):
    if x:
        return -1
    else:
        return 1    
sym=pd.read_csv("C:\\Users\\abhin\\Downloads\\russell-1000-index-08-07-2023.csv")['Symbol'].to_numpy()
lo=0
li=[]
for i in range(999):
    try:
        profit=np.zeros(473)
        d1=pd.read_csv("C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\"+sym[i]+".csv")
        d1['mean']=d1['open'].rolling(30).mean()
        d1=d1[29:-1]
        d1['profit']= d1['open']>d1['mean']
        kp=d1['profit'].to_numpy()
        try:
            for k in range(473):
                if kp[k]:
                    profit[k]=-1
                else:
                    profit[k]=1
            data.loc[len(data)]=profit                
        except:
            lo+=1
            print(len(kp))
            print (sym[i])
            li.append(sym[i])
    except:
        print(sym[i]+' Failed')        
print(lo)
print(li)