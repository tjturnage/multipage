"""
This runs the buoys plot
"""
from datetime import datetime, timedelta

import itertools
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

from config import DATA_DIRECTORY as SOURCE_DATA_DIRECTORY
from config import BUOY_DICT, CMAN_DICT, STYLE_DICT
from config import WINDSPEED_TITLE, WAVE_SUB_PREFIX, WAVE_SUB_SUFFIX
#from layouts import layout_buoys
startup = True
now = datetime.utcnow()
start = now - timedelta(hours=3)

wind_range = dict[0, 15]
wave_range = [0,5]

#wind_hover = "<b>%{text}</b><br><br>GDP per Capita: %{x:$,.0f}<br>%{y:.0%}<br><extra></extra>"

BUOY_IDS = list(BUOY_DICT.keys())
CMAN_IDS = list(CMAN_DICT.keys())

titles=[]
for key in BUOY_DICT.keys():
    buoy_title = BUOY_DICT[key]['title']
    this_title = f'{WAVE_SUB_PREFIX}{buoy_title}{WAVE_SUB_SUFFIX}'
    titles.append(this_title)
    titles.append(WINDSPEED_TITLE) 

subplot_titles = tuple(titles)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

#layout = layout_buoys

dash.register_page(__name__,
    path='/buoys2',
    title='Buoys',
    name='Buoys',
    order=8)

def layout():
    return html.Div([
    dbc.Container([
            dbc.Row(dbc.Col(html.H2("Buoy Observations"))),
            dbc.Row(dbc.Col(dcc.Graph(id='graph', figure={}))),
            dcc.Interval(
                id='interval',
                interval=60 * 1000,  # in milliseconds
                n_intervals=0,
                max_intervals=-1)
        ]),
    #dcc.Store(id='buoy-data-dict')
    ])

new_buoy_data = {}
for buoy in BUOY_IDS:
    buoy_dataframe = None
    source = f'{SOURCE_DATA_DIRECTORY}/{buoy}.csv'
    buoy_dataframe = pd.read_csv(source, parse_dates=['dts'], index_col='dts')
    new_buoy_data[buoy] = buoy_dataframe
print(new_buoy_data)
fig = make_subplots(
    rows=6, cols=2,
    shared_xaxes=True,
    vertical_spacing=0.05,
    horizontal_spacing=0.04,
    row_heights=[0.25,0.25,0.25,0.25,0.25,0.25],
    subplot_titles=subplot_titles)
for i, buoy in enumerate(BUOY_IDS):
    row = i + 1
    fig.add_trace(go.Scatter(x=new_buoy_data[buoy].index, y=new_buoy_data[buoy]['WVHT'], name=BUOY_DICT[buoy]['title'], line=STYLE_DICT['WVHT']['line']), row=row, col=1)

fig.update_xaxes(range=[start, now])
fig.update_yaxes(range=wave_range)
fig.update_yaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
fig.update_layout(showlegend=False)

elements = ['WSPD']
for buoy, element in itertools.product(BUOY_IDS, elements):
    fig.add_trace(go.Scatter(x=new_buoy_data[buoy].index, y=new_buoy_data[buoy][element], name=BUOY_DICT[buoy]['title'], line=STYLE_DICT[element]['line']), row=BUOY_DICT[buoy]['row'], col=2)

elements = ['GST']
for buoy, element in itertools.product(BUOY_IDS, elements):
    fig.add_trace(go.Scatter(x=new_buoy_data[buoy].index, y=new_buoy_data[buoy][element], mode='markers', name=BUOY_DICT[buoy]['title'], line=STYLE_DICT[element]['line']), row=BUOY_DICT[buoy]['row'], col=2)
fig.update_xaxes(range=[start, now])
#fig.update_yaxes(range=[0, max_speed])
#fig.update_yaxes(range=wind_range)
fig.update_xaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
fig.update_layout(showlegend=False)
fig.update_layout(
    autosize=False,
    width=1200,
    height=800,
    margin=dict(
        l=10,
        r=10,
        b=10,
        t=40,
        pad=4
    )
)

fig.update_layout(template='plotly_dark')
# fig.update_layout(yaxis1 = wave_range)
# fig.update_layout(yaxis2 = wind_range)
# fig.update_layout(yaxis3 = wave_range)
# fig.update_layout(yaxis4 = wind_range)
# fig.update_layout(yaxis5 = wave_range)
# fig.update_layout(yaxis6 = wind_range)
# fig.update_layout(yaxis7 = wave_range)
# fig.update_layout(yaxis8 = wind_range)
# fig.update_layout(yaxis9 = wave_range)
# fig.update_layout(yaxis10 = wind_range)
# fig.update_layout(yaxis11 = wave_range)
# fig.update_layout(yaxis12 = wind_range)
fig.update_layout(hovermode="x unified")
fig.update_layout(title_x=0.01)


@app.callback(Output('buoy-data-dict', 'data'),
              Input('interval-component', 'n_intervals'))
def update_buoys(n):
    """
    this reads the data from the csv files
    """
    new_buoy_data = {}

    for buoy in BUOY_IDS:
        buoy_dataframe = None
        source = f'{SOURCE_DATA_DIRECTORY}/{buoy}.csv'
        buoy_dataframe = pd.read_csv(source, parse_dates=['dts'], index_col='dts')
        new_buoy_data[buoy] = buoy_dataframe
    print(new_buoy_data)
    return new_buoy_data

@app.callback(Output('graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph(n):
    """_summary_

    Args:
        new_buoy_data (_type_): _description_
    """

    fig = make_subplots(
        rows=6, cols=2,
        shared_xaxes=True,
        vertical_spacing=0.05,
        horizontal_spacing=0.04,
        row_heights=[0.25,0.25,0.25,0.25,0.25,0.25],
        subplot_titles=subplot_titles)
    for i, buoy in enumerate(BUOY_IDS):
        row = i + 1
        fig.add_trace(go.Scatter(x=new_buoy_data[buoy].index, y=new_buoy_data[buoy]['WVHT'], name=BUOY_DICT[buoy]['title'], line=STYLE_DICT['WVHT']['line']), row=row, col=1)

    fig.update_xaxes(range=[start, now])
    fig.update_yaxes(range=wave_range)
    fig.update_yaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
    fig.update_layout(showlegend=False)

    elements = ['WSPD']
    for buoy, element in itertools.product(BUOY_IDS, elements):
        fig.add_trace(go.Scatter(x=new_buoy_data[buoy].index, y=new_buoy_data[buoy][element], name=BUOY_DICT[buoy]['title'], line=STYLE_DICT[element]['line']), row=BUOY_DICT[buoy]['row'], col=2)

    elements = ['GST']
    for buoy, element in itertools.product(BUOY_IDS, elements):
        fig.add_trace(go.Scatter(x=new_buoy_data[buoy].index, y=new_buoy_data[buoy][element], mode='markers', name=BUOY_DICT[buoy]['title'], line=STYLE_DICT[element]['line']), row=BUOY_DICT[buoy]['row'], col=2)
    fig.update_xaxes(range=[start, now])
    #fig.update_yaxes(range=[0, max_speed])
    fig.update_yaxes(range=wind_range)
    fig.update_xaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
    fig.update_layout(showlegend=False)
    fig.update_layout(
        autosize=False,
        width=1200,
        height=800,
        margin=dict(
            l=10,
            r=10,
            b=10,
            t=40,
            pad=4
        )
    )

    fig.update_layout(template='plotly_dark')
    # fig.update_layout(yaxis1 = wave_range)
    # fig.update_layout(yaxis2 = wind_range)
    # fig.update_layout(yaxis3 = wave_range)
    # fig.update_layout(yaxis4 = wind_range)
    # fig.update_layout(yaxis5 = wave_range)
    # fig.update_layout(yaxis6 = wind_range)
    # fig.update_layout(yaxis7 = wave_range)
    # fig.update_layout(yaxis8 = wind_range)
    # fig.update_layout(yaxis9 = wave_range)
    # fig.update_layout(yaxis10 = wind_range)
    # fig.update_layout(yaxis11 = wave_range)
    # fig.update_layout(yaxis12 = wind_range)
    fig.update_layout(hovermode="x unified")
    fig.update_layout(title_x=0.01)
    return fig

