import dash
from dash import dcc, html
from .callbacks import register_callbacks
import os

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Graph(id='progress-graph'),
    dcc.Interval(id='interval', interval=30000, n_intervals=0)
])

register_callbacks(app)
