import dash_core_components as dcc
import dash_html_components as html
from view import jitter_bar_fatality_chart

def return_tab2_result():
        tab2_result = html.Div([
                dcc.Dropdown(
                id='dd_incident_selection',
                options=[
                {'label': 'Incidents', 'value': 'incident'},
                {'label': 'Fatal incidents', 'value': 'fatal_accident'},
                {'label': 'Fatalities', 'value': 'fatalities'},
                {'label': 'Lethality', 'value': 'lethality'},

                ],
                value='incident',
                style=dict(width='45%',
                        verticalAlign="middle")
                        ),

                html.Iframe(
                        sandbox='allow-scripts',
                        id='jitter_bar_chart',
                        height='1000',
                        width='1500',
                        style={'border-width': '0'},
                        srcDoc = jitter_bar_fatality_chart.return_jitter_bar_fatality_chart().to_html()
                        ),

                ])
        return tab2_result 
