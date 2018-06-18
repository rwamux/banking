import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go

df_age = pd.read_csv("https://github.com/rwamux/banking/blob/master/resources/santander_by_age.csv",index_col=0) 
df_s = pd.read_csv("https://github.com/rwamux/banking/blob/master/resources/santander_by_segment.csv",index_col=0)
df_act = pd.read_csv("https://github.com/rwamux/banking/blob/master/resources/santander_by_activity.csv",index_col=0)
df_g = pd.read_csv("https://github.com/rwamux/banking/blob/master/resources/santander_by_gender.csv",index_col=0)


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
        
        ) ,
        dcc.Graph(
        id = 'bar-by-segment',
        figure={
                'data':[
                    go.Bar(
                        x=df_s.index.values,
                        y=df_s[i],
                        name=i  
                    
                    )for i in df_s.columns
                
                ],
                'layout':go.Layout(
                        title = "Customer Segmentation of Products",
                        barmode='stack'
                
                )
        }
        
        ),
        dcc.Graph(
        id = 'bar-by-activity',
        figure={
                'data':[
                    go.Bar(
                        x=df_act.index.values,
                        y=df_act[i],
                        name=i
                    )for i in df_act.columns
                ],
                'layout':go.Layout(
                    title="Purchased product types by customer activity index",
                    barmode='stack'
                )
        }
        
        
        ),
        dcc.Graph(
        id = 'bar-by-gender',
        figure={
                'data':[
                    go.Bar(
                        x=df_g.index.values,
                        y=df_g[i],
                        name=i
                    )for i in df_g.columns
                ],
                'layout':go.Layout(
                       title="Purchased products by sex",
                       barmode='stack' 
                )
        }
        )
         
    ]) 
    



app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
if __name__ == '__main__':
    app.run_server(debug=True)
