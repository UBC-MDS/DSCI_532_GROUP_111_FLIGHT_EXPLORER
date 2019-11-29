import altair as alt
import sys
from model import data_wrangle

def return_jitter_bar_fatality_chart(value = "incident"):
    plot = alt.Chart(data_wrangle.chart_1_data).encode(
        alt.X(f"{value}_period:N", title = "Time period"),
        alt.Y(f"{value}_value:Q", title = "Count"))

    plot1 = alt.layer(plot.mark_boxplot(size=200, opacity=.4) + plot.mark_point()
       ).configure_title(fontSize=18
    ).configure_legend(labelFontSize=13
    ).configure_axis(labelFontSize=11, titleFontSize=14
    ).properties(width = 800, height = 600, title = f"{value} of airline incidents")
    
    return plot1