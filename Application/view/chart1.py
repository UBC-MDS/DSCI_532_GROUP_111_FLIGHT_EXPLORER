import altair as alt
from Application.model import data_wrangle

plot = alt.Chart(data_wrangle.chart_1_data).encode(
    alt.X("variable", title = "Time period"),
    alt.Y("value", title = "Count"))

plot1 = alt.layer(plot.mark_boxplot(size=200, opacity=.4) + plot.mark_point()
   ).configure_title(fontSize=18
).configure_legend(labelFontSize=13
).configure_axis(labelFontSize=11, titleFontSize=14
).properties(width = 800, height = 600, title = "Lethality of airline incidents")