from dash import dcc
from dash import html

import dash_bootstrap_components as dbc

layout_buoys = html.Div([
    dbc.Container([
            dbc.Row(dbc.Col(html.H2("Buoy Observations"))),
            dbc.Row(dbc.Col(dcc.Graph(id='graph', figure={}))),
            dcc.Interval(
                id='interval',
                interval=60 * 1000,  # in milliseconds
                n_intervals=0,
                max_intervals=-1)
        ]),
    dcc.Store(id='buoy-data-dict')

    ])