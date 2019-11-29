import dash
import dash_core_components as dcc
import dash_html_components as html
import altair as alt
from view import tab1, tab2, incident_horizontal_bar_chart, jitter_bar_fatality_chart
from dash.dependencies import Input, Output

app = dash.Dash(__name__, assets_folder='assets')
app.config['suppress_callback_exceptions'] = True
server = app.server

app.title = 'Dash app with pure Altair HTML'

app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tab-1', children=[
    dcc.Tab(label='Fatality rates per billion by airlines', value='tab-1'),
    dcc.Tab(label='Counts of different categories of incidents', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])

def render_content(tab):
    if tab == 'tab-1':
        return tab1.return_tab1_result()
    elif tab == 'tab-2':
        return tab2.return_tab2_result()


@app.callback(Output('horizontal_bar_chart_iframe', 'srcDoc'),
              [Input('radio-items', 'value')])
def render_incident_horizontal_bar_chart(value):
    return incident_horizontal_bar_chart.return_fatality_bar_chart(value).to_html()


@app.callback(Output('jitter_bar_chart', 'srcDoc'),
              [Input('dd_incident_selection', 'value')])
def render_jitter_bar_fatality_chart(value):
    return jitter_bar_fatality_chart.return_jitter_bar_fatality_chart(value).to_html()

    
if __name__ == '__main__':
    app.run_server(debug=True)