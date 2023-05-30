"""
This runs the climo plot
"""
from pathlib import Path
from datetime import datetime, date
import dash
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import polars as pl
#import pandas as pd
import plotly.express as px
from .side_bar import sidebar

p = Path('/home/tjturnage')
q = p / 'multipage' / 'data' / 'climate.txt'

if q.exists():
    DATA = q
else:
    DATA = "data/climate.txt"

df = pl.read_csv('/home/tjturnage/multipage/data/climate.txt', has_header=True, null_values=["M"])
df = df.with_columns(
    [
    pl.col("pcpn").str.replace("T", "0.001"),
    pl.col("date").str.strptime(pl.Date, format='%Y-%m-%d', strict=False)
    ]
    )

out = df.select(
[
    pl.col("date"),
    pl.col("maxt").cast(pl.Int32).alias("max_int"),
    pl.col("mint").cast(pl.Int32).alias("min_int"),
    pl.col("avgt").cast(pl.Float32).alias("avg"),
    pl.col("pcpn").cast(pl.Float32).alias("precip"),
])


dash.register_page(__name__,
    title='GRR Climo',
    name='GRR Climo', order=2)

def layout():
    """
    This defines the dashboard
    """
    return dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H1("Choose Temperature Range")),
                dbc.Col(html.H1("Variable"), width=2),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.RangeSlider(-20, 110, 5, value=[30,80],
                               id='range'),
                ),

                dbc.Col(
                    dcc.Dropdown(["max_int", "min_int", "avg"], "max_int",
                               id='element'),
                    width=2
                ),
            ],
            className="mb-4",
        ),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="chart")
        ]),
    ]),

])

@callback(
    Output("chart", "figure"),
    Input('range', 'value'),
    Input('element','value'),
)
def update_graph(range, el):
    """
    doc string test
    """

    
    return px.histogram(x=out.select(el).filter(pl.col(el) <= range[1]).filter(pl.col(el) >= range[0]).to_series(),range_y=[0, 1200])
