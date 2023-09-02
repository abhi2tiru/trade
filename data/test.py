import pandas as pd
import plotly.express as px
import plotly.graph_objects as gop
data=pd.read_csv('tstat.csv')
data=data.sort_values(by=['tstat'],ascending=False)
data=data[0:10]
print(data)
name=data['name'].to_numpy()
fig=gop.Figure()
for i in name:
    m=pd.read_csv(i+'.csv')
    m[i]=m[i].cumsum()
    fig.add_trace(gop.Scatter( x=m['date'],y=m[i],name=i))
get=[31,95,157,219,283,346,408,470]
data=pd.read_csv('rsi_44.csv')
date=data['date'].to_numpy()
got=[]
for i in get:
    got.append(date[i])
for i in got:
    fig.add_vline(i)
fig.show()    