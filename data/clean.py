import pandas as pd 
data=pd.read_csv("C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\A.csv")
print(data)
'''
data=pd.read_csv("C:\\Users\\abhin\\Downloads\\russell-1000-index-08-07-2023.csv")
symbol=data['Symbol'].to_numpy()[:-1]
sym=[]
for i in range(1000):
    m='C:\\Users\\abhin\\Downloads\\tickers-20230818T020407Z-001\\tickers\\'+symbol[i]+'.csv'
    try:
        tick=pd.read_csv(m)
        if len(tick)==l:
            sym.append(symbol[i])
    except:
        print(symbol[i])
data=pd.DataFrame({'tickers':sym})      
print(data)        '''