import altair as alt

from model import data_wrangle


def return_fatality_bar_chart(value=None):
    """
    creates an altair chart object for the plot of the fatality barchart.
    Parameters
    ----------
    value: the value passed in from the radio buttons.
     "0", "1", and "2" for "first-world", "non-first-world", and "both" respectively.

    Returns
    -------
    Altair.Chart object of the bar chart.
    """
    value = '0' if value is None else value
    plot2 = alt.Chart(data_wrangle.chart_2_data,
                      title="Number of fatalities for airlines that had an incident between 1985 and 2014"
                      ).mark_bar().encode(
        alt.Y("airline:N",
              title="Airline (* includes regional subsidiaries)",
              sort=alt.EncodingSortField(
                  field="total_fatalities_per_b_avail_seat_km",
                  order="ascending")),
        alt.X("total_fatalities_per_b_avail_seat_km:Q",
              axis=alt.Axis(
                  title="Rate of fatalities per billion available seat kilometers")),
        tooltip=[alt.Tooltip(shorthand="total_fatalities_per_b_avail_seat_km:Q",
                             title="count of fatalities")]
    ).configure_mark(color="blue"
                     ).configure_title(fontSize=18
                                       ).configure_legend(labelFontSize=13
                                                          ).configure_axis(labelFontSize=11,
                                                                           titleFontSize=14
                                                                           ).properties(width=800,
                                                                                        height=600)

    if value != "2":
        if value == "0":
            color_range = ["blue", "grey"]
        else:
            color_range = ["gray", "blue"]
        plot2 = alt.Chart(data_wrangle.chart_2_data,
                          title="Number of fatalities for airlines that had an incident between 1985 and 2014"
                          ).mark_bar().encode(
            alt.Y("airline:N",
                  title="Airline (* includes regional subsidiaries)",
                  sort=alt.EncodingSortField(
                      field="total_fatalities_per_b_avail_seat_km",
                      order="ascending")),
            alt.X("total_fatalities_per_b_avail_seat_km:Q",
                  axis=alt.Axis(
                      title="Rate of fatalities per billion available seat kilometers")),

            alt.Color("first_world",
                      title=None,
                      scale=alt.Scale(domain=["First World", "Other"],
                                      range=color_range)),
            tooltip=[alt.Tooltip(shorthand="total_fatalities_per_b_avail_seat_km:Q",
                                 title="count of fatalities")]
        ).configure_title(fontSize=18
                          ).configure_legend(labelFontSize=13
                                             ).configure_axis(labelFontSize=11,
                                                              titleFontSize=14
                                                              ).properties(width=800, height=600)
    return plot2


return_fatality_bar_chart(0)
