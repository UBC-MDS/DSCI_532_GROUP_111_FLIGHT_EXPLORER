import dash_core_components as dcc
import dash_html_components as html
from view import jitter_bar_fatality_chart

def return_tab2_result():
        tab2_result = html.Div([
                dcc.Dropdown(
                id='dd-chart1',
                options=[
                {'label': 'Incidents', 'value': '0'},
                {'label': 'Fatal incidents', 'value': '1'},
                {'label': 'Fatalities', 'value': '2'},
                {'label': 'Lethality', 'value': '3'},

                ],
                value='0',
                style=dict(width='45%',
                        verticalAlign="middle")
                        ),

                html.Iframe(
                        sandbox='allow-scripts',
                        id='plot1',
                        height='1000',
                        width='1500',
                        style={'border-width': '0'},
                        srcDoc = jitter_bar_fatality_chart.return_jitter_bar_fatality_chart().to_html()
                        ),

                ])
        return tab2_result 
