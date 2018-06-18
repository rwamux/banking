import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go

df =  pd.read_csv("https://github.com/rwamux/banking/blob/master/resources/santander_sclean.csv",index_col=0)
df_a = df.loc[:,['age']].join(df.loc[:,'savings':'direct_debit'])
df_age = df_a.groupby(pd.cut(df_a['age'],[0,18,25,35,45,55, pd.np.inf],labels=['0-18','18-25','25-35','35-45','45-55','55-inf'],right=False).astype(str)).sum()
del df_age['age']
df_age = df_age.T


app = dash.Dash(__name__)
server = app.server
app.layout = html.Div(children=[
        html.H4('Customer Analytics dashboard'),
        dcc.Graph(
        id = 'bar-by-age',
        figure = {
                'data':[
                    go.Bar(
                        x = df_age.index.values,
                        y = df_age[i],
                        name = i
                     
                    )for i in df_age.columns
                
                ],
                'layout':go.Layout(
                        title="Customer age distribution for each product",
                        barmode='stack',
                        xaxis={'title':'Product names'},
                        yaxis={'title':'Total number of customers'}
                        )
        }
        
        ) 
         
    ]) 
    



app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
if __name__ == '__main__':
    app.run_server(debug=True)
