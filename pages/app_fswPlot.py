"""
This runs the fsw plot
"""
from pathlib import Path
import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np
from . import ids
from .side_bar import sidebar

p = Path('/home/tjturnage')
q = p / 'multipage' / 'data' / 'fsw_output.txt'

if q.exists():
    DATA = q
else:
    DATA = "data/fsw_output.txt"


dash.register_page(__name__,
title='FSW_plot',
name='FSW_plot',order=2)

dts = []
product = []
with open(DATA,'r', encoding='utf_8') as src:
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
    #df_temp[p] = np.where(df_temp['product'] == p,1,0).cumsum()
    df_temp[p] = np.where(df_temp['product'] == p,1,0).sum()
df_temp['count'] = 1
df_temp['month'] = df_temp.index.month
df_temp['Year'] = df_temp.index.year
#print(df_temp)


def layout():
    """
    This defines the dashboard
    """
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
                                id=ids.FSW_PRODUCT_CHOSEN
,
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


@callback(Output("line_chart_new", "figure"), Input(ids.FSW_PRODUCT_CHOSEN, "value"),suppress_callback_exceptions=True)
def update_graph_card(products):
    """
    doc string test
    """
    if len(products) == 0:
        return dash.no_update
    df_filtered = df_temp[df_temp["product"].isin(products)]



    fig = px.line(
        df_filtered,
        x=df_filtered.index,
        y=products,
        color="product",
        labels={"Graffiti": "Graffiti incidents (avg)"},
    ).update_traces(mode="lines+markers")
    return fig

