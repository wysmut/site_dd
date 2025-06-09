import dash
from dash import dcc, html
import plotly.express as px
import requests

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Graph(id='progress-graph'),
    dcc.Interval(id='interval', interval=30000, n_intervals=0)
])
