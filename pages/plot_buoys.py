"""
This runs the buoys plot
"""
#from pathlib import Path
from datetime import datetime, timedelta
from pathlib import Path
import itertools
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
#from . import ids
#from .side_bar import sidebar

now = datetime.utcnow()
start = now - timedelta(hours=3)


SOURCE_DATA_DIRECTORY = '/home/tjturnage/multipage/data'
if 'pyany' in Path().absolute().parts:
    SOURCE_DATA_DIRECTORY = 'C:/data/scripts/pyany/data'


BUOY_DICT = {'45024': {'title': 'Ludington Buoy', 'row': 1},           
         '45161': {'title': 'Muskegon Buoy', 'row': 2},
         '45029': {'title': 'Holland Buoy', 'row': 3},
         '45168': {'title': 'South Haven Buoy', 'row': 4},
         '45210': {'title': 'Central LM', 'row': 5},
         '45007': {'title': 'LM South Buoy', 'row': 6}
}

CMAN_DICT = {'LDTM4': {'title': 'Ludington', 'row': 2},
            'MKGM4': {'title': 'Muskegon', 'row': 4},
            'HLNM4': {'title': 'Holland', 'row': 6},
            'SVNM4': {'title': 'South Haven', 'row': 8},
             }

new_buoy_data = {}

BUOY_IDS = list(BUOY_DICT.keys())
BUOY_TITLES = []
for key in BUOY_DICT:
    BUOY_TITLES.append(BUOY_DICT[key]['title'])

dash.register_page(__name__,
    path='/buoys2',
    title='Buoys',
    name='Buoys',
    order=8)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
app.layout = html.Div([
    dbc.Container([
            dbc.Row(dbc.Col(html.H2("Buoy Observations"))),
            dbc.Row(dbc.Col(dcc.Graph(id='graph'))),
            dcc.Interval(
                id='interval',
                interval=60 * 1000,  # in milliseconds
                n_intervals=0,
                max_intervals=-1)
        ]),

    ])



@app.callback(Output('graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def start_buoys(n):
    """
    this reads the data from the csv files
    """
new_buoy_data = {}
max_height = 0
max_speed = 0
for buoy in BUOY_IDS:
    buoy_dataframe = None
    source = f'{SOURCE_DATA_DIRECTORY}/{buoy}.csv'
    buoy_dataframe = pd.read_csv(source, parse_dates=['dts'], index_col='dts')
    max_height = max(max_height, buoy_dataframe['WVHT'].max())
    max_speed = max(max_speed, buoy_dataframe['GST'].max())
    new_buoy_data[buoy] = buoy_dataframe
if max_height > 15:
    max_wave = 20
elif max_height > 10:
    max_wave = 15
elif max_height > 5:
    max_wave = 10
else:
    max_wave = 5

#print(new_buoy_data)

#@app.callback(Output('graph', 'figure'),
#              Input('interval-component', 'n_intervals'))
def layout():
    return html.Div([
        dbc.Container([
            dbc.Row(dbc.Col(html.H2("Buoy Observations"))),
            dbc.Row(dbc.Col(dcc.Graph(id='graph', figure=fig))),
            dcc.Interval(
                id='interval',
                interval=60 * 1000,  # in milliseconds
                n_intervals=0,
                max_intervals=-1)
        ]),

    ])

marker_dict = dict(color='white', size=3)
#y = list(this_df['GST'])
#marker_dict = dict(list(map(set_color, y)))
wave_line_dict = dict(color='#00CCCC', width=3)
wind_line_dict = dict(color='gray', width=3)
#wind_hover = "<b>%{text}</b><br><br>GDP per Capita: %{x:$,.0f}<br>%{y:.0%}<br><extra></extra>"

WINDSPEED_TITLE = 'Wind Speed and Gust (kt)'
WAVE_SUB_PREFIX = '<b><span style="color:#DDDD33;">'
WAVE_SUB_SUFFIX = '</b> Wave Height (ft)'

#for b in BUOY_TITLES:
#    subplot_title += f'{WAVE_SUBLOT_PREFIX}{b}{WAVE_SUBLOT_SUFFIX}, {WINDSPEED_TITLE}, '
subplot_titles=(f'{WAVE_SUB_PREFIX}Ludington{WAVE_SUB_SUFFIX}', WINDSPEED_TITLE,
                    f'{WAVE_SUB_PREFIX}Muskegon{WAVE_SUB_SUFFIX}', WINDSPEED_TITLE,
                    f'{WAVE_SUB_PREFIX}Holland{WAVE_SUB_SUFFIX}', WINDSPEED_TITLE,
                    f'{WAVE_SUB_PREFIX}South Haven{WAVE_SUB_SUFFIX}', WINDSPEED_TITLE,
                    f'{WAVE_SUB_PREFIX}Central LM<{WAVE_SUB_SUFFIX}', WINDSPEED_TITLE,
                    f'{WAVE_SUB_PREFIX}South LM{WAVE_SUB_SUFFIX}', WINDSPEED_TITLE)
fig = make_subplots(
    rows=6, cols=2,
    shared_xaxes=True,
    vertical_spacing=0.05,
    horizontal_spacing=0.04,
    row_heights=[0.25,0.25,0.25,0.25,0.25,0.25],
    subplot_titles=(subplot_titles))
for i, buoy in enumerate(BUOY_IDS):
    row = i + 1
    fig.add_trace(go.Scatter(x=new_buoy_data[buoy].index, y=new_buoy_data[buoy]['WVHT'], name=BUOY_TITLES[i], line=wave_line_dict), row=row, col=1)

fig.update_xaxes(range=[start, now])
#fig.update_yaxes(range=[0, max_wave])
fig.update_yaxes(range=[0, 5])
fig.update_yaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
fig.update_layout(showlegend=False)

elements = ['WSPD','GST']
for buoy, element in itertools.product(BUOY_IDS, elements):
    fig.add_trace(go.Scatter(x=new_buoy_data[buoy].index, y=new_buoy_data[buoy][element], name=BUOY_DICT[buoy]['title'], line=wind_line_dict), row=BUOY_DICT[buoy]['row'], col=2)

fig.update_xaxes(range=[start, now])
#fig.update_yaxes(range=[0, max_speed])
fig.update_yaxes(range=[0, 15])
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
#fig2.update_layout(template='plotly_dark')
#wave_range = dict(range=[0,max_wave])

wind_range = dict(range=[0, 15])
wave_range = dict(range=[0,5])
#fig.update_layout(height=800, width=600, title_text="Wave Height (ft)")
fig.update_layout(yaxis1 = wave_range)
fig.update_layout(yaxis2 = wind_range)
fig.update_layout(yaxis3 = wave_range)
fig.update_layout(yaxis4 = wind_range)
fig.update_layout(yaxis5 = wave_range)
fig.update_layout(yaxis6 = wind_range)
fig.update_layout(yaxis7 = wave_range)
fig.update_layout(yaxis8 = wind_range)
fig.update_layout(yaxis9 = wave_range)
fig.update_layout(yaxis10 = wind_range)
fig.update_layout(yaxis11 = wave_range)
fig.update_layout(yaxis12 = wind_range)
fig.update_layout(hovermode="x unified")
fig.update_layout(title_x=0.01)

@app.callback(Output('graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_buoys(n):
    """
    this reads the data from the csv files
    """
    new_buoy_data = {}
    max_height = 0
    max_speed = 0
    for buoy in BUOY_IDS:
        buoy_dataframe = None
        source = f'{SOURCE_DATA_DIRECTORY}/{buoy}.csv'
        buoy_dataframe = pd.read_csv(source, parse_dates=['dts'], index_col='dts')
        max_height = max(max_height, buoy_dataframe['WVHT'].max())
        max_speed = max(max_speed, buoy_dataframe['GST'].max())
        new_buoy_data[buoy] = buoy_dataframe
    if max_height > 15:
        max_wave = 20
    elif max_height > 10:
        max_wave = 15
    elif max_height > 5:
        max_wave = 10
    else:
        max_wave = 5
    return new_buoy_data, max_wave, max_speed
