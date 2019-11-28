import dash_html_components as html
import dash_core_components as dcc
import sys
sys.path.append("..")

import view.chart2 as chart2

tab1_result = html.Div([
            dcc.RadioItems(
        options=[
        {'label': 'First world', 'value': '##### Lise, you can pick your value here'},
        {'label': 'Non first world', 'value': '##### Lise, you can pick your value here'},
        {'label': 'Both', 'value': '##### Lise, you can pick your value here'}
        ],
        value='##### Lise, this is the default value for radio button'),
            html.Iframe(
                    sandbox='allow-scripts',
                    id='plot',
                    height='1000',
                    width='1500',
                    style={'border-width': '0'},
                    
                    srcDoc =  chart2.return_plot_2().to_html()
        
                    ),
        ])