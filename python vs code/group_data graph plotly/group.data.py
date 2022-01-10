import pandas as pd
import plotly.express as px
f = pd.read_csv('data_viz.csv')
fig = px.scatter(f, x='Age', y='Duration (min)', color='Gender', marginal_y='violin',
                 marginal_x='box', template='simple_white')
fig.show()

