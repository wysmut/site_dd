import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import psycopg2
import os

app = dash.Dash(name)

app.layout = html.Div([
html.H1('Статистика тестирования'),
dcc.Graph(id='score-distribution'),
dcc.Interval(
id='interval-component',
interval=60*1000,
n_intervals=0
)
])

def get_db_connection():
conn = psycopg2.connect(
dbname=os.getenv('DB_NAME'),
user=os.getenv('DB_USER'),
password=os.getenv('DB_PASSWORD'),
host=os.getenv('DB_HOST'),
port=os.getenv('DB_PORT')
)
return conn

@app.callback(
Output('score-distribution', 'figure'),
Input('interval-component', 'n_intervals')
def update_graph(n):
try:
conn = get_db_connection()
df = pd.read_sql_query("SELECT * FROM core_result;", conn)
conn.close()

    if df.empty:
        return px.bar(title='Нет данных')
    
    fig = px.histogram(df, x='score', nbins=20, title='Распределение баллов')
    return fig
except:
    return px.bar(title='Ошибка подключения')

server = app.server
