import dash
import dash_core_components as dcc
import dash_html_components as html
import altair as alt
from dash.dependencies import Input, Output
from model import data_wrangle

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
    


####### Lise, you can insert your function calls for your plots in the following 

def return_plot_1(key = 'First World'): 
    plot2 = alt.Chart((data_wrangle.chart_1_data), title = "Number of fatalities for airlines that had an incident between 1985 and 2014").mark_bar().encode(
        alt.Y("airline:O", title="Airline (* includes regional subsidiaries)", sort=alt.EncodingSortField(field = "total_fatalities_per_b_avail_seat_km", order="ascending")),
        alt.X("total_fatalities_per_b_avail_seat_km:Q", axis = alt.Axis(title = "Rate of fatalities per billion available seat kilometers")),
        color=alt.condition(
        alt.datum.first_world == key,  
        alt.value('orange'),
        alt.value('steelblue')  
    )
    ).configure_title(fontSize=18
    ).configure_legend(labelFontSize=13
    ).configure_axis(labelFontSize=11, titleFontSize=14
    ).properties(width = 800, height = 600)
    return plot2


def return_plot_2(category = 'incidents'):
    
    if category == 'lethality':
        chart = data_wrangle.chart_2_lethality
    elif category == 'incidents':
        chart = data_wrangle.chart_2_incidents
    elif category == 'fatalities':
        chart = data_wrangle.chart_2_fatalities
    elif category == 'fatal_accidents':
        chart = data_wrangle.chart_2_fatal_accidents
        
    plot_0 = alt.Chart(chart).encode(
        alt.X("variable", title = "Time period"),
        alt.Y("value", title = "Count"))

    plot = alt.layer(plot_0.mark_boxplot(size=200, opacity=.4) + plot_0.mark_point()
       ).configure_title(fontSize=18
    ).configure_legend(labelFontSize=13
    ).configure_axis(labelFontSize=11, titleFontSize=14
    ).properties(width = 800, height = 600, title = "Different incidents in two periods")
    
    return plot




app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tab-1', children=[
    dcc.Tab(label='Fatality rates per billion by airlines', value='tab-1'),
    dcc.Tab(label='Counts of different categories of incidents', value='tab-2'),
    ]),
    html.Div(id='tabs-content-example')
]

)


@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs', 'value')])

def render_content(tab):

    if tab == 'tab-1':
        return html.Div([
            dcc.RadioItems(
        options=[
        {'label': 'First world', 'value': '##### Lise, you can pick your value here'},
        {'label': 'Non first world', 'value': '##### Lise, you can pick your value here'},
        {'label': 'Both', 'value': '##### Lise, you can pick your value here'}
        ],
        value='##### Lise, this is the default value for radio button'),
            html.Iframe(
                    sandbox='allow-scripts',
                    id='plot1',
                    height='1000',
                    width='1500',
                    style={'border-width': '0'},
                    
                    srcDoc = return_plot_1().to_html()
        
                    ),
        ])
    elif tab == 'tab-2':
        return html.Div([
            #Insert code for tab2 plot here
            dcc.Dropdown(
        id='dd-chart1',
        options=[
        {'label': 'Incidents', 'value': '##### Lise, you can pick your value here'},
        {'label': 'Fatal incidents', 'value': '##### Lise, you can pick your value here'},
        {'label': 'Fatalities', 'value': '##### Lise, you can pick your value here'},
        {'label': 'Lethality', 'value': '##### Lise, you can pick your value here'},

        ],
        value='##### Lise, this is the default value for drop dowm',
        style=dict(width='45%',
                verticalAlign="middle")
                ),

        html.Iframe(
                sandbox='allow-scripts',
                id='plot2',
                height='1000',
                width='1500',
                style={'border-width': '0'},
                
                srcDoc = return_plot_2().to_html()
                
                ),

        ])



# @app.callback(

# dash.dependencies.Output('plot1', 'srcDoc'),
# [dash.dependencies.Input('dd-chart1', 'value')])

# def update_plot(incident_type):
#     '''
    
#     '''
#     updated_plot = return_plot_2().to_html()
#     return updated_plot

    
if __name__ == '__main__':
    app.run_server(debug=True)