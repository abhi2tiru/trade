import pandas as pd
import plotly.graph_objects as go

fig=go.Figure()

m=pd.read_csv('aroon_5cd0.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['aroon_5'],name='aroon_5_cd0'))

m=pd.read_csv('aroon_5od0.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['aroon_5'],name='aroon_5_od0'))

m=pd.read_csv('aroon_5od.5.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['aroon_5'],name='aroon_5_d.5'))

m=pd.read_csv('aroon_5cd-.5.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['aroon_5'],name='aroon_5_d-.5'))

m=pd.read_csv('aroon_5od1.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['aroon_5'],name='aroon_5_d1'))

m=pd.read_csv('aroon_5od-1.csv')
fig.add_trace(go.Scatter( x=m['date'],y=m['aroon_5'],name='aroon_5_d-1'))

fig.show()