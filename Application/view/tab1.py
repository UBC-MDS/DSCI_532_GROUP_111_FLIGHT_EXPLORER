import dash_html_components as html
import dash_core_components as dcc
from view import incident_horizontal_bar_chart

def return_tab1_result(value = "0"):
    tab1_result = html.Div([
                dcc.RadioItems(
                    id = "radio-items",
                    options=[
                    {'label': 'First world', 'value': '0'},
                    {'label': 'Non first world', 'value': '1'},
                    {'label': 'Both', 'value': '2'}
                    ],
                    value='0'),
                html.Iframe(
                        sandbox='allow-scripts',
                        id='horizontal_bar_chart_iframe',
                        height='1000',
                        width='1500',
                        style={'border-width': '0'},
                        srcDoc = incident_horizontal_bar_chart.return_fatality_bar_chart(value).to_html()
                        )])
    return tab1_result