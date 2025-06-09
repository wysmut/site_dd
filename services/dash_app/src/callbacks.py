from dash import Dash, Input, Output
import plotly.express as px
import requests

def register_callbacks(app):
    @app.callback(
        Output('progress-graph', 'figure'),
        Input('interval', 'n_intervals'),
        Input('url', 'search')
    )
    def update_graph(n, search):
        user_id = search.split('=')[1] if search and '=' in search else '1'
        
        try:
            response = requests.get(f"http://backend/api/results/?user_id={user_id}")
            data = response.json()
            
            if not data:
                return px.bar(title="Нет данных")
                
            df = pd.DataFrame(data)
            fig = px.line(
                df, 
                x='date_taken', 
                y='score', 
                title='Прогресс обучения',
                labels={'score': 'Баллы', 'date_taken': 'Дата теста'}
            )
            return fig
        except Exception as e:
            return px.bar(title=f"Ошибка: {str(e)}")
