import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
from .side_bar import sidebar
import pandas as pd
from pathlib import Path
import numpy as np
#import os

#os.chdir('C:/data/scripts/Forecast_Search_Wizard/')


p = Path('/home/tjturnage')
q = p / 'multipage' / 'assets' / 'fsw_output.txt'

if q.exists():
    data = q
else:
    data = "assets/fsw_output.txt"


dash.register_page(__name__,
title='FSW_plot',
name='FSW_plot',order=2)

dts = []
product = []
with open(data,'r') as src:
    for line in src.readlines():
        if line[0] in ('0','1'):
            values = line.split('\t')
            dts.append(values[0])
            product.append(values[1][1:])

#print(dts,product)
dts_pd = pd.to_datetime(dts,format='%m-%d-%Y %H:%M', infer_datetime_format=False)
data = {'dts':dts_pd, 'product':product}
df_temp = pd.DataFrame(data)
df_temp.set_index('dts', inplace=True)
unique_prods = list(df_temp['product'].unique())
print(unique_prods)
for p in unique_prods:
    df_temp[p] = np.where(df_temp['product'] == p,1,0).cumsum()


def layout():
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col([sidebar()], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),
                    dbc.Col(
                        [
                            html.H3(
                                "Cumulative sum of product mentions",
                                style={"textAlign": "center"},
                            ),
                            dcc.Dropdown(
                                id="product_chosen",
                                options=df_temp["product"].unique(),
                                value=["AFDGRR", "AFDAPX"],
                                multi=True,
                                style={"color": "black"},
                            ),
                            html.Hr(),
                            dcc.Graph(id="line_chart_new", figure={}),
                        ],
                        xs=8,
                        sm=8,
                        md=10,
                        lg=10,
                        xl=10,
                        xxl=10,
                    ),
                ]
            )
        ]
    )


@callback(Output("line_chart_new", "figure"), Input("product_chosen", "value"),suppress_callback_exceptions=True)
def update_graph_card(products):
    if len(products) == 0:
        return dash.no_update
    else:
        pees = []
        for p in products:
            pees.append(list(df_temp[p]))

        fig = px.line(
            df_temp,
            x=df_temp.index,
            y=pees,
            labels={"Mentions": "Mentions (sum)"},
        ).update_traces(mode="lines+markers")
        return fig

