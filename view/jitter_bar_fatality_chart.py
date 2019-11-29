import altair as alt

from model import data_wrangle


def return_jitter_bar_fatality_chart(value=None):
    """
    generates an altair plot based on the value input.

    Parameters
    ----------
    value: one of 'incident', 'fatal_accident', 'fatalities', 'lethality'.
        defaults to 'incident'

    Returns
    -------
    an alt.Chart object of the rendered plot.
    """
    value = "incident" if value is None else value
    value_title_dict = {'incident': "Incidents",
                        'fatal_accident': "Fatal Accidents",
                        'fatalities': "Fatalities",
                        'lethality': "Lethality"}

    bar_plot = alt.Chart(data_wrangle.chart_1_data).encode(
        alt.X(f"{value}_period:N", title="Time period"),
        alt.Y(f"{value}_value:Q", title="Count"))

    jitter_plot = alt.Chart(data_wrangle.chart_1_data).encode(
        alt.X(f"{value}_period:N", title="Time period"),
        alt.Y(f"{value}_value:Q", title="Count"),
        tooltip=["airline", f"{value}_value:Q"])

    plot1 = alt.layer(bar_plot.mark_boxplot(size=200,
                                            opacity=.4) +
                      jitter_plot.mark_point()
                      ).configure_title(fontSize=18
                                        ).configure_legend(labelFontSize=13
                                                           ).configure_axis(labelFontSize=12,
                                                                            titleFontSize=24
                                                                            ).properties(width=800,
                                                                                         height=600,
                                                                                         title=f"Count of Airline {value_title_dict[value]}")

    return plot1
