#!/usr/bin/env python
# coding: utf-8

# In[116]:


import requests
import pandas as pd

url='https://api.covid19api.com/total/country/pakistan'

r = requests.get(url)

data=pd.DataFrame.from_dict(r.json())


# In[83]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np


# In[84]:


app = dash.Dash()


# In[85]:


# Creating Data
np.random.seed(42)
random_x=np.random.randint(1,101,100)
random_y=np.random.randint(1,101,100)


# In[170]:


data['New Confirmed']=data['Confirmed'].diff()
data['New Deaths']=data['Deaths'].diff()
data['New Recovered']=data['Recovered'].diff()
data

# In[224]:



app.layout=html.Div([
    
    html.H1('Pakistan COVID19 - Daily Tracker made in Dash Plotly', style={'textAlign': 'center'}),
    html.H2('Data Updated as of '+data['Date'].max(), style={'textAlign': 'center'}),
    
            html.Div([
        dcc.Graph(id='KPI_1', 
         figure={'data':[
             go.Indicator(
            mode = "number+delta",
            value = data['Active'].iloc[-1],
             title='Total Active Cases',
#             number = {'prefix': "$"},
            delta = {'position': "top", 'reference': data['Active'].iloc[-2]})]},
            style={'width': '33%', 'display': 'inline-block'}
         )
        
        ,
        
        dcc.Graph(id='KPI_2', 
         figure={'data':[
             go.Indicator(
            mode = "number+delta",
            value = data['Recovered'].iloc[-1],
             title='Total Recovered Cases',
#             number = {'prefix': "$"},
            delta = {'position': "top", 'reference': data['Recovered'].iloc[-2]})]},
            style={'width': '33%', 'display': 'inline-block'}
         )
        
        ,
        
        dcc.Graph(id='KPI_3', 
         figure={'data':[
             go.Indicator(
            mode = "number+delta",
            value = data['Deaths'].iloc[-1],
             title='Total Death Cases',
#             number = {'prefix': "$"},
            delta = {'position': "top", 'reference': data['Deaths'].iloc[-2]})]},
            style={'width': '33%', 'display': 'inline-block'}
         )
        
])
    
    ,    
    
    html.Div([
        
        dcc.Graph(id='BarChart1', 
         figure={'data':[
             go.Bar(
             x=data['Date'].iloc[-60:],
             y=data['New Confirmed'].iloc[-60:],
             )],
          'layout':go.Layout(title='New Confirmed Cases',)},
            style={'width': '60%', 'display': 'inline-block'}
         )
        
        ,
        
        dcc.Graph(id='PieChart1', 
         figure={'data':[
             go.Pie(
             values=data[['Deaths','Recovered','Active']].iloc[-1],
             labels=['Deaths','Recovered','Active'],
             marker=dict(colors=['grey','green','red'], line=dict(color='#000000', width=2)),
                 hole=.3,
             )],
          'layout':go.Layout(title='Total Position',)},
            style={'width': '40%', 'display': 'inline-block'}
         )
        
])
    

])


# In[ ]:


if __name__ == '__main__':
    app.run_server()

