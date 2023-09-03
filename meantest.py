import pandas as pd
import plotly.graph_objects as go

fig=go.Figure()

m=pd.read_csv('mean_7cd0.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['mean_7'],name='mean_7_cd0'))

m=pd.read_csv('mean_7od0.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['mean_7'],name='mean_7_od0'))

m=pd.read_csv('mean_7od.5.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['mean_7'],name='mean_7_d.5'))

m=pd.read_csv('mean_7od-.5.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['mean_7'],name='mean_7_d-.5'))

m=pd.read_csv('mean_7od1.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['mean_7'],name='mean_7_d1'))

m=pd.read_csv('mean_7od-1.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['mean_7'],name='mean_7_d-1'))

fig.show()