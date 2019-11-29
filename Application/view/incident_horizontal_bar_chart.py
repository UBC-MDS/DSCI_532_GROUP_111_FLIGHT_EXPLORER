import altair as alt
import sys
from model import data_wrangle

def return_fatality_bar_chart(value = '0'): 
    plot2 = alt.Chart(data_wrangle.chart_2_data, title = "Number of fatalities for airlines that had an incident between 1985 and 2014").mark_bar().encode(
        alt.Y("airline:O", title="Airline (* includes regional subsidiaries)", sort=alt.EncodingSortField(field = "total_fatalities_per_b_avail_seat_km", order="ascending")),
        alt.X("total_fatalities_per_b_avail_seat_km:Q", axis = alt.Axis(title = "Rate of fatalities per billion available seat kilometers")),
        alt.Color("first_world", title = None, scale=alt.Scale(scheme="category20"))
    ).configure_title(fontSize=18
    ).configure_legend(labelFontSize=13
    ).configure_axis(labelFontSize=11, titleFontSize=14
    ).properties(width = 800, height = 600)
    return plot2


