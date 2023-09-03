import pandas as pd
import plotly.graph_objects as go

fig=go.Figure()

m=pd.read_csv('band_14_cd0.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['band_14'],name='band_14_cd0'))

m=pd.read_csv('band_14_od0.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['band_14'],name='band_14_od0'))

m=pd.read_csv('band_14_d.5.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['band_14'],name='band_14_d.5'))

m=pd.read_csv('band_14_d-.5.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['band_14'],name='band_14_d-.5'))

m=pd.read_csv('band_14_d1.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['band_14'],name='band_14_d1'))

m=pd.read_csv('band_14_d-1.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['band_14'],name='band_14_d-1'))

fig.show()