import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from view import incident_horizontal_bar_chart


def return_fatality_rates_bar_chart_result(value=None):
    """
    returns the html div that's rendered into the tab.
    Parameters
    ----------
    value: the value passed in by the radio button.

    Returns
    -------
    the html div to be rendered into the tab.

    """
    value = "0" if value is None else value

    tab1_result = dbc.Container([
        dbc.Row([
            dbc.Col([dcc.RadioItems(
                id="radio-items",
                options=[
                    {'label': 'First world ', 'value': '0'},
                    # {'label': 'Non first world ', 'value': '1'},  # We decide to remove the 'Non-first world', I still keep it here just in case
                    {'label': 'All', 'value': '2'}

                ],
                value='0',
                style=dict(width='45%',
                           verticalAlign="middle")),
                           dbc.Jumbotron([dcc.Markdown("""This bar chart shows the adjusted fatality rate, calculated as number of fatal incidents, 
                           normalized by the total distance each airline flys, as wells as the nubmer of seats per flight."""), 
                           dcc.Markdown("""Hover over each bar to see each airline's adjusted fatality rate."""),
                           dcc.Markdown("""The airlines are grouped by the economic status of their orginating country, 
                           where countries of a sufficient economic status is designated [**first world**](https://www.nationsonline.org/oneworld/first_world.htm).""")]),
                    ],
                width="2"),
            dbc.Col(html.Iframe(
                sandbox='allow-scripts',
                id='horizontal_bar_chart_iframe',
                height='1000',
                width='1500',
                style={'border-width': '0'},
                srcDoc=incident_horizontal_bar_chart.return_fatality_bar_chart(value).to_html()
            ),
                width=10)
        ])
    ],
        fluid=True)

    return tab1_result
