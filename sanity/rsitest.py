import pandas as pd
import plotly.graph_objects as go

fig=go.Figure()

m=pd.read_csv('rsi_6_cd0.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['rsi_6'],name='rsi_6_cd0'))

m=pd.read_csv('rsi_6_od0.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['rsi_6'],name='rsi_6_od0'))

m=pd.read_csv('rsi_6_od.5.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['rsi_6'],name='rsi_6_d.5'))

m=pd.read_csv('rsi_6_od-.5.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['rsi_6'],name='rsi_6_d-.5'))

m=pd.read_csv('rsi_6_od1.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['rsi_6'],name='rsi_6_d1'))

m=pd.read_csv('rsi_6_od-1.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['rsi_6'],name='rsi_6_d-1'))

fig.show()