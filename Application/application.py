import dash
import dash_core_components as dcc
import dash_html_components as html
import altair as alt
# import sys
# sys.path.append()
from view import tab1, tab2
# import view.tab2 as tab2
from dash.dependencies import Input, Output

app = dash.Dash(__name__, assets_folder='assets')
app.config['suppress_callback_exceptions'] = True
server = app.server

app.title = 'Dash app with pure Altair HTML'


def make_plot():
    def mds_special():
        font = "Arial"
        axisColor = "#000000"
        gridColor = "#DEDDDD"
        return {
            "config": {
                "title": {
                    "fontSize": 24,
                    "font": font,
                    "anchor": "start", # equivalent of left-aligned.
                    "fontColor": "#000000"
                },
                'view': {
                    "height": 300, 
                    "width": 400
                },
                "axisX": {
                    "domain": True,
                    #"domainColor": axisColor,
                    "gridColor": gridColor,
                    "domainWidth": 1,
                    "grid": False,
                    "labelFont": font,
                    "labelFontSize": 12,
                    "labelAngle": 0, 
                    "tickColor": axisColor,
                    "tickSize": 5, # default, including it just to show you can change it
                    "titleFont": font,
                    "titleFontSize": 16,
                    "titlePadding": 10, # guessing, not specified in styleguide
                    "title": "X Axis Title (units)", 
                },
                "axisY": {
                    "domain": False,
                    "grid": True,
                    "gridColor": gridColor,
                    "gridWidth": 1,
                    "labelFont": font,
                    "labelFontSize": 14,
                    "labelAngle": 0, 
                    #"ticks": False, # even if you don't have a "domain" you need to turn these off.
                    "titleFont": font,
                    "titleFontSize": 16,
                    "titlePadding": 10, # guessing, not specified in styleguide
                    "title": "Y Axis Title (units)", 
                    # titles are by default vertical left of axis so we need to hack this 
                    #"titleAngle": 0, # horizontal
                    #"titleY": -10, # move it up
                    #"titleX": 18, # move it to the right so it aligns with the labels 
                },
            }
                }

    # register the custom theme under a chosen name
        alt.themes.register('mds_special', mds_special)

        # enable the newly registered theme
        alt.themes.enable('mds_special')
        #alt.themes.enable('none') # to return to default
        



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

# @app.callback(Output('plot1', 'srcDoc'),
#               [Input('dd-chart1', 'value')])
# def new_tab2_graph(value):
#     return tab2.return_tab2_result(value)  


    
if __name__ == '__main__':
    app.run_server(debug=True)