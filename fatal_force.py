import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_columns', None)

df_hh_income = pd.read_csv('Median_Household_Income_2015.csv', encoding="windows-1252")
df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")
df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")

df_hh_income.fillna("", inplace=True)
df_fatalities.fillna("", inplace=True)
df_pct_poverty['poverty_rate'].replace('-', 0, inplace=True)
df_pct_completed_hs['percent_completed_hs'].replace('-', 0, inplace=True)

## POVERTY BAR CHART
df_pct_poverty.set_index(['Geographic Area', 'City'], inplace=True)
df_pct_poverty['poverty_rate'] = df_pct_poverty['poverty_rate'].astype(float)

poverty_by_state = df_pct_poverty.groupby(level='Geographic Area').mean()
poverty_by_state = poverty_by_state.sort_values(by=['poverty_rate'], ascending=False)

poverty_fig, poverty_bar_chart = plt.subplots()

poverty_rates = poverty_bar_chart.bar(x=poverty_by_state.index, height=poverty_by_state['poverty_rate'])
poverty_bar_chart.set_ylabel("Poverty Rate")
poverty_bar_chart.set_xlabel("State")

plt.show()

## GRADUATION BAR CHART
df_pct_completed_hs.set_index(['Geographic Area', 'City'], inplace=True)
df_pct_completed_hs['percent_completed_hs'] = df_pct_completed_hs['percent_completed_hs'].astype(float)

completed_hs_by_state = df_pct_completed_hs.groupby(level='Geographic Area').mean()
completed_hs_by_state = completed_hs_by_state.sort_values(by=['percent_completed_hs'], ascending=True)

graduation_fig, graduation_bar_chart = plt.subplots()

graduation_rates = graduation_bar_chart.bar(x=completed_hs_by_state.index, height=completed_hs_by_state['percent_completed_hs'])
graduation_bar_chart.set_ylabel("Graduation Rate")
graduation_bar_chart.set_xlabel("State")

plt.show()