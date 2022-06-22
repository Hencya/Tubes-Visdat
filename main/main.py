import pandas as pd
from os.path import dirname, join
from script.cummulative import *
from script.daily import *

from bokeh.plotting import curdoc
from bokeh.models.widgets import Tabs

df = pd.read_csv(
    join(dirname(__file__), "data", "Indonesia_coronavirus_daily_data.csv"), index_col=0
).dropna()
df = df.reset_index(level=0)
df["Date"] = pd.to_datetime(df["Date"], format="%Y/%m/%d")
tab1 = daily(df)
tab2 = cummulative(df)
tab = Tabs(tabs=[tab1, tab2])

curdoc().title = "Indonesia Corona"
curdoc().add_root(tab)
