import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd


########### Define your variables ######
myheading = "AirBnbs in Mahanttan is very expensive!!!"
tabtitle = 'AirBnb Price by Areas in New York City'
filename = 'CleanedData.csv'
sourceurl = 'https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data/'
githublink = 'https://github.com/ylcgu/project1'

########### Set up the data
df = pd.read_csv(filename)

results= df.groupby(['area'])['price'].mean()
print(results.sort_values(ascending=False))

# In[143]:

import plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True) #this is to diplay figures in notebook
import plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import*


# In[150]:


# displa with plotly
mydata = go.Bar(
 x =results.index,
y= results.values,
marker={'color': ['blue', 'red', 'green', 'yellow']})
mylayout = go.Layout(
title ='Airbnb Price Per Night',
xaxis= dict(title='Areas_in_NYC'),
yaxis= dict(title='Price_per_night')
)
myfigure = go.Figure([mydata],mylayout)
myfigure

# In[157]:

results2= df.groupby(['room','area'])['room'].count()
print(results.sort_values(ascending=False))


# In[175]:


results2= df.groupby(["room", "area"])["room"].count().sort_values(ascending=False)
results2 = pd.DataFrame(results2)
results2


mydata2 = go.Bar(x = results2.loc['Entire home/apt'].index,
                y = results2.loc['Entire home/apt']['room'],
               name = 'Entire home/apt', )
mydata3 = go.Bar(x = results2.loc['Private room'].index,
                y = results2.loc['Private room']['room'],
               name = 'Private room', )
mydata4 = go.Bar(x = results2.loc['Shared room'].index,
                y = results2.loc['Shared room']['room'],
               name = 'Shared room', )
mylayout2 = go.Layout(title = 'Geographic distribution of rooms',
xaxis= dict(title='Areas_in_NYC'),
yaxis= dict(title='Rooms number')
)

fig=go.Figure(data=[mydata2,mydata2,mydata3], layout=mylayout2)
iplot(fig)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
