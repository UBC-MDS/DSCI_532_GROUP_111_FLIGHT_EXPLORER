# Load packages
import pandas as pd
import altair as alt
import numpy as np

#load dataset
data = pd.read_csv("model/airline-safety.csv")

#add incidents/accidents/fatalities for both time periods together
data["total_incidents"] = data["incidents_85_99"] + data["incidents_00_14"]

#calculate available seat km per week in billions
data["avail_seat_km_per_week_billions"] = data["avail_seat_km_per_week"]/1000000000

#include only airlines that had incidents
no_zeros = data[data["incidents_85_99"] > 0]
no_zeros_either = no_zeros[no_zeros["incidents_00_14"] > 0]

#create dataset to use for plot2 
data2 = no_zeros_either.drop(columns=["avail_seat_km_per_week", "incidents_85_99", "fatal_accidents_85_99", "incidents_00_14", "fatal_accidents_00_14", "total_incidents"])
data2["fatalities_85_99"] = data2["fatalities_85_99"]/data2["avail_seat_km_per_week_billions"]
data2["fatalities_00_14"] = data2["fatalities_00_14"]/data2["avail_seat_km_per_week_billions"]
data2 = data2.drop(columns="avail_seat_km_per_week_billions")
data2["fatalities_85_99"] = data2["fatalities_85_99"] + data2["fatalities_00_14"]
data2 = data2.drop(columns = "fatalities_00_14")
data2 = data2.rename(columns = {"fatalities_85_99" : "total_fatalities_per_b_avail_seat_km"})
data2 = data2.reset_index().drop(columns="index")

#classify first world countries based on https://www.nationsonline.org/oneworld/first_world.htm
data2["first_world"] = np.zeros(len(data2))
data2["first_world"] = "Other"
data2["first_world"][3,4,6, 7,8, 9, 10, 11, 12, 14, 16, 20, 22, 23, 24, 28, 30, 32, 34, 36, 40, 41, 42] = "First World"

#plot1
plot1 = alt.Chart(data).mark_point().encode(
    alt.X("avail_seat_km_per_week_billions:Q", scale=alt.Scale(type='log', base=2), title = "Available seat kilometers per week (in billion kms)"),
    alt.Y("total_incidents:Q", title = "Number of incidents")
).configure_mark(color="dodgerblue", opacity = .9
).configure_title(fontSize=16
).configure_axis(labelFontSize=11, titleFontSize=14
).properties(width=700, height=350, title="Number of incidents as a function of opportunity for incidents")

#plot2
plot2 = alt.Chart(data2.reset_index(), title = "Number of fatalities for airlines that had an incident between 1985 and 2014").mark_bar().encode(
    alt.Y("airline:O", title="Airline (* includes regional subsidiaries)", sort=alt.EncodingSortField(field = "total_fatalities_per_b_avail_seat_km", order="ascending")),
    alt.X("total_fatalities_per_b_avail_seat_km:Q", axis = alt.Axis(title = "Rate of fatalities per billion available seat kilometers")),
    alt.Color("first_world", title = None, scale=alt.Scale(scheme="category20"))
).configure_title(fontSize=18
).configure_legend(labelFontSize=13
).configure_axis(labelFontSize=11, titleFontSize=14
).properties(width = 800, height = 600)


