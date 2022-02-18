import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("p108data.csv")

mob = df["Avg Rating"].tolist()
fig = ff.create_distplot([mob],["Avg Rating"],show_hist = False)
fig.show()
