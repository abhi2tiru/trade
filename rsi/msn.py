import pandas as pd
import numpy as np
df=pd.read_csv('AAPL.csv')
df['timestamp']=df['timestamp'].apply(lambda x:pd.to_datetime(x*1000000))
print(df)