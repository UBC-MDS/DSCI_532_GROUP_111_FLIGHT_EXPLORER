import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from view import jitter_bar_fatality_chart


def return_incident_jitter_boxplot_result(value=None):
    """
    Returns the html div to be rendered into the counts of different categories tab.
    Parameters
    ----------
    value: the value passed in by the drop-down button.

    Returns
    -------
    an html div of the jitter/boxplot to be rendered inside the tab.

    """
    value = 'incident' if value is None else value

    tab2_result = dbc.Container([
        dbc.Row([
            dbc.Col([dcc.RadioItems(

                id='dd_incident_selection',
                options=[
                    {'label': 'Incidents', 'value': 'incident'},
                    {'label': 'Fatal incidents', 'value': 'fatal_accident'},
                    {'label': 'Fatalities', 'value': 'fatalities'},
                    {'label': 'Lethality', 'value': 'lethality'},
                ],    
                value='incident',
                style=dict(width='45%',
                           verticalAlign="middle")),
            dbc.Jumbotron([dcc.Markdown("""This box plot with scatter shows One of four statistics, over the two periods of 1985-1999, and 2000- 2014."""), 
                           dcc.Markdown("""**Incidents**: the number of Incidents, both fatal and non-fatal."""),
                           dcc.Markdown("""**Fatal Incidents**: the number of Incidents, involving fatalities."""),
                           dcc.Markdown("""**Fatalities**: the number of fatalities per airline during the two periods"""),
                           dcc.Markdown("""**Lethality**: the proportion of incidents that are fatal incidents"""),
                           dcc.Markdown("""Hover over each scatterplot point to see each airline and it's corresponding statistic.""")]),
            ],
                width="2"),
            dbc.Col(html.Iframe(
                sandbox='allow-scripts',
                id='jitter_bar_chart',
                height='1000',
                width='1500',
                style={'border-width': '0'},
                srcDoc=jitter_bar_fatality_chart.return_jitter_bar_fatality_chart(value).to_html()
            ),
                width="8")
        ])
    ],
        fluid=True)
    return tab2_result
