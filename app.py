import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go

df_age =  pd.read_csv("https://github.com/rwamux/banking/blob/master/resources/santander_by_age.csv",index_col=0,skiprows=1,names=['0-18','18-25','25-35','35-45','45-55','55-inf'])



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
