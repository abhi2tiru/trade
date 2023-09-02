import pandas as pd
import numpy as np

days=6
tdays=503-days
# read company
data=pd.read_csv('AAPL.csv')
open=data['open'].to_numpy()
#initilize two arrays for aroon up and  aroon down
up =np.zeros(tdays)
down=np.zeros(tdays)
for i in range(tdays):
    up[i]=100*np.argmax(open[i:i+days])/days
    down[i]=100*np.argmin(open[i:i+days])/days
print(pd.DataFrame({'up':up,'down':down}))
