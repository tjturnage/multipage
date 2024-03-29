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

STYLE_DICT = {'GST': {'line': dict(color='white', width=0), 'marker': dict(color='white', size=3)},
              'WVHT': {'line': dict(color='#00CCCC', width=3), 'marker': dict(color='#00CCCC', size=3)},
              'WSPD': {'line': dict(color='gray', width=3), 'marker': dict(color='gray', size=0)}
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
min_height = 100
min_speed = 100
for buoy in BUOY_IDS:
    buoy_dataframe = None
    source = f'{SOURCE_DATA_DIRECTORY}/{buoy}.csv'
    buoy_dataframe = pd.read_csv(source, parse_dates=['dts'], index_col='dts')
    max_height = max(max_height, buoy_dataframe['WVHT'].max())
    max_speed = max(max_speed, buoy_dataframe['GST'].max())
    min_height = min(min_height, buoy_dataframe['WVHT'].min())
    min_speed = min(min_speed, buoy_dataframe['GST'].min())
    new_buoy_data[buoy] = buoy_dataframe

#max_height = max(max_height, buoy_dataframe['WVHT'].max())
#max_speed = max(max_speed, buoy_dataframe['GST'].max())
#min_height = min(min_height, buoy_dataframe['WVHT'].min())
#min_speed = min(min_speed, buoy_dataframe['GST'].min())
max_wave = max_height + 2 - (max_height % 2)
#min_wave = min_height - 2 - (min_height % 2)
min_wave = max(min_height - 1 , 0)
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
                interval=3 * 60 * 1000,  # in milliseconds
                n_intervals=0,
                max_intervals=-1)
        ]),

    ])
now = datetime.utcnow()
start = now - timedelta(hours=3)
marker_dict = dict(color='white', size=3)
#y = list(this_df['GST'])
#marker_dict = dict(list(map(set_color, y)))
wave_line_dict = dict(color='#00CCCC', width=3)
wind_line_dict = dict(color='gray', width=3)
#wind_hover = "<b>%{text}</b><br><br>GDP per Capita: %{x:$,.0f}<br>%{y:.0%}<br><extra></extra>"

WINDSPEED_TITLE = 'Wind Speed and Gust (kt)'
WAVE_SUB_PREFIX = '<b><span style="color:#DDDD33;">'
WAVE_SUB_SUFFIX = '</b> Wave Height (ft)'

titles=[]
for b in BUOY_TITLES:
    this_title = f'{WAVE_SUB_PREFIX}{b}{WAVE_SUB_SUFFIX}'
    titles.append(this_title)
    titles.append(WINDSPEED_TITLE)

subplot_titles = tuple(titles)

fig = make_subplots(
    rows=6, cols=2,
    shared_xaxes=True,
    vertical_spacing=0.05,
    horizontal_spacing=0.04,
    row_heights=[0.25,0.25,0.25,0.25,0.25,0.25],
    subplot_titles=subplot_titles)
    for buoy, element in itertools.product(BUOY_IDS, elements):
        buoy_dataframe = new_buoy_data[buoy]
        buoy_element = buoy_dataframe[element]
        buoy_title = BUOY_DICT[buoy]['title']
        buoy_color = BUOY_DICT[buoy]['color']
        this_line_dict = {}
        this_line_dict['color'] = BUOY_DICT[buoy]['color']
        this_line_dict['width'] = BUOY_DICT[buoy]['line_width']
        this_line_dict['dash'] = 'solid'
        if element == 'WVHT':
            fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, text=buoy_title, line=this_line_dict, hovertemplate = '%{y:.2f} ft'), row=1, col=1)   
        if element == 'WSPD':
            fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, text=buoy_title, line=this_line_dict, hovertemplate = '%{y:.0f} kt'), row=2, col=1)
        if element == 'GST':
            this_marker_dict=dict(color=buoy_color, size=5*BUOY_DICT[buoy]['line_width'])
            fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, mode="markers", marker=this_marker_dict, hovertemplate='G %{y:.0f} kt'), row=2, col=1)
    fig.update_xaxes(range=[start_time, end_time])
    fig.update_xaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
    fig.update_yaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
    fig.update_layout(showlegend=False)
    fig.update_layout(
        autosize=False,
        width=1200,
        height=800,
        margin=dict(
        l=15,
        r=15,
        b=10,
        t=50,
        pad=6
        )
    )

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
fig.add_hline(y=4, line_dash="dot", line_width=1, line=dict(color='rgba(255, 100, 100, 0.7)'), row="all", col=1)
              #line_color="#ee3333")#, annotation_text="SCA", 
              #annotation_position="bottom right")
fig.add_hline(y=18, line_dash="dot", line_width=1, line=dict(color='rgba(255, 255, 100, 0.7)'), row="all", col=2)
              #line_color="#ee3333")#, annotation_text="SCA", 
              #annotation_position="bottom right")

@app.callback(Output('graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_buoys(n):
    """
    this reads the data from the csv files
    """
    new_buoy_data = {}
    max_height = 0
    max_speed = 0
    min_height = 100
    min_speed = 100
    for buoy in BUOY_IDS:
        buoy_dataframe = None
        source = f'{SOURCE_DATA_DIRECTORY}/{buoy}.csv'
        buoy_dataframe = pd.read_csv(source, parse_dates=['dts'], index_col='dts')
        max_height = max(max_height, buoy_dataframe['WVHT'].max())
        max_speed = max(max_speed, buoy_dataframe['GST'].max())
        min_height = min(min_height, buoy_dataframe['WVHT'].min())
        min_speed = min(min_speed, buoy_dataframe['GST'].min())
        new_buoy_data[buoy] = buoy_dataframe
    
    max_wave = max_height + 2 - (max_height % 2)
    #min_wave = min_height - 2 - (min_height % 2)
    min_wave = max(min_height -1 , 0)

    return new_buoy_data, max_wave, min_wave, max_speed