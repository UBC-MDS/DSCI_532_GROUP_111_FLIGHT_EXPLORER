import dash
import dash_core_components as dcc
import dash_html_components as html
from view import chart2
from dash.dependencies import Input, Output
import sys
sys.path.append('../')
app = dash.Dash(__name__, assets_folder='assets')
server = app.server

app.title = 'Dash app with pure Altair HTML'

app.layout = html.Div([
    html.Iframe(
        sandbox='allow-scripts',
        id='plot',
        height='500',
        width='700',
        style={'border-width': '0'},
        srcDoc=chart2.plot2.to_html() 
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)