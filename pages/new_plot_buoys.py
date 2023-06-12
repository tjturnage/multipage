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


SOURCE_DATA_DIRECTORY = '/home/tjturnage/multipage/data'
if 'pyany' in Path().absolute().parts:
    SOURCE_DATA_DIRECTORY = 'C:/data/scripts/pyany/data'

opac = 0.85
lw = 1.5
BUOY_DICT = {'45024': {'title': 'Ludington Buoy', 'color': f'rgba(255, 255, 255, {opac})', 'line_width': lw},           
         '45161': {'title': 'Muskegon Buoy', 'color': f'rgba(200, 200, 255, {opac})', 'line_width': lw},
         '45029': {'title': 'Holland Buoy', 'color': f'rgba(150, 150, 255, {opac})', 'line_width': lw},
         '45168': {'title': 'South Haven Buoy', 'color': f'rgba(112, 112, 255, {opac})', 'line_width': lw},
         '45210': {'title': 'Central LM', 'color': f'rgba(80, 80, 255, {opac})', 'line_width': lw},
         '45007': {'title': 'LM South Buoy', 'color': f'rgba(30, 30, 255, {opac})', 'line_width': lw}
         }

CMAN_DICT = {'LDTM4': {'title': 'Ludington'},
            'MKGM4': {'title': 'Muskegon'},
            'HLNM4': {'title': 'Holland'},
            'SVNM4': {'title': 'South Haven'},
             }


STYLE_DICT = {'GST': {'line': dict(width=0), 'marker': dict(size=2)},
              'WVHT': {'line': dict(width=1), 'marker': dict(size=2)},
              'WSPD': {'line': dict(width=1), 'marker': dict(size=0)}
              }



BUOY_IDS = list(BUOY_DICT.keys())
BUOY_TITLES = []
for key in BUOY_DICT:
    BUOY_TITLES.append(BUOY_DICT[key]['title'])

def update_times():
    """
    defines the x axis range based on the current time

    Returns:
        start_time: datetime object : xmin for graph
    """
    now = datetime.utcnow()
    start_time = now - timedelta(hours=3)
    end_time = now + timedelta(minutes=10)
    return now, start_time, end_time

def update_buoys():
    """
    creates a dictionary of dataframes by reading a csv file
    for each buoy id in BUOY_IDS
    """
    this_new_buoy_data = {}
    this_max_height = 0
    this_max_speed = 0
    this_min_height = 100
    this_min_speed = 100
    for buoy in BUOY_IDS:
        this_buoy_dataframe = None
        this_source = f'{SOURCE_DATA_DIRECTORY}/{buoy}.csv'
        this_buoy_dataframe = pd.read_csv(this_source, parse_dates=['dts'], index_col='dts')
        this_max_height = max(this_max_height, this_buoy_dataframe['WVHT'].max())
        this_max_speed = max(this_max_speed, this_buoy_dataframe['GST'].max())
        this_min_height = min(this_min_height, this_buoy_dataframe['WVHT'].min())
        this_min_speed = min(this_min_speed, this_buoy_dataframe['GST'].min())
        this_new_buoy_data[buoy] = this_buoy_dataframe
    
    this_max_wave = this_max_height
    this_min_wave = this_min_height - 1
    final_min_wave = max(this_min_wave, 0)
    new_max_speed = this_max_speed + 5 - (this_max_speed % 5)
    new_min_speed = this_min_speed - 5 + (this_min_speed % 5)
    final_min_speed = max(new_min_speed, 0)

    return this_new_buoy_data, this_max_wave, final_min_wave, new_max_speed, final_min_speed

dash.register_page(__name__,
    path='/buoys3',
    title='New Buoys',
    name='New Buoys',
    order=9)


def layout():
    """_summary_

    Returns:
        _type_: _description_
    """
    return html.Div([
        dbc.Container([
            dbc.Row(dbc.Col(html.H2("Buoy Observations"))),
            dbc.Row(dbc.Col(html.H5(id='update-time'))),
            dbc.Row(dbc.Col(dcc.Graph(id='layout-graph'))),
            dcc.Interval(
                id='interval',
                interval=10 * 60 * 1000,  # in milliseconds
                n_intervals=0,
                max_intervals=-1)
        ]),

    ])

@dash.callback(Output('update-time', 'children'),
          Input('interval', 'n_intervals'))
def update_time(n):
    return f'Updated:  {datetime.utcnow().strftime(" %H:%M UTC -- %b %d, %Y")}'

@dash.callback(Output('layout-graph', 'figure'),
          Input('interval', 'n_intervals'))
def update_graph(n):
    now,start_time,end_time = update_times()
    new_buoy_data, max_wave, min_wave, max_speed, min_speed = update_buoys()
    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        row_heights=[0.4,0.3],
        subplot_titles=('Wave Height (ft)', 'Wind Speed and Gust (kt)'))
    elements = ['WVHT','WSPD','GST']
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
            fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, line=this_line_dict, hovertemplate = '%{y:.2f} ft'), row=1, col=1)   
        if element == 'WSPD':
            fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, line=this_line_dict, hovertemplate = '%{y:.0f} kt'), row=2, col=1)
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
    caution = 'rgba(255, 255, 100, 0.7)'
    danger = 'rgba(255, 10, 100, 0.7)'
    fig.update_layout(template='plotly_dark')
    wind_range = dict(range=[min_speed, max_speed])
    wave_range = dict(range=[min_wave, max_wave])
    fig.update_layout(yaxis1 = wave_range)
    fig.update_layout(yaxis2 = wind_range)
    fig.update_layout(hovermode="x unified")
    fig.update_layout(title_x=0.08)
    #fig.add_hline(y=4, line=dict(dash="solid", width=2, color=danger), row=1, col=1)
    #fig.add_hline(y=18, line=dict(dash="solid", width=2, color=caution), row=2, col=1)
    fig.add_hrect(y0=min_wave, y1=3, fillcolor="green", opacity=0.10, line_width=0, row=1, col=1)
    fig.add_hrect(y0=3, y1=4, fillcolor="yellow", opacity=0.10, line_width=0, row=1, col=1)
    fig.add_hrect(y0=4, y1=6, fillcolor="red", opacity=0.10, line_width=0, row=1, col=1)
    fig.add_hrect(y0=6, y1=20, fillcolor="pink", opacity=0.20, line_width=0, row=1, col=1)
    
    fig.add_hrect(y0=min_speed, y1=18, fillcolor="green", opacity=0.10, line_width=0, row=2, col=1)
    fig.add_hrect(y0=18, y1=22, fillcolor="yellow", opacity=0.10, line_width=0, row=2, col=1)
    fig.add_hrect(y0=22, y1=33, fillcolor="red", opacity=0.10, line_width=0, row=2, col=1)
    fig.add_hrect(y0=33, y1=40, fillcolor="pink", opacity=0.20, line_width=0, row=2, col=1)
    #fig.add_hline(y=22, line=dict(dash="solid", width=2, color=danger), row=2, col=1)
    fig.add_vline(x=now, line=dict(dash="solid", width=2, color='white'), row=1, col=1)
    fig.add_vline(x=now, line=dict(dash="solid", width=2, color='white'), row=2, col=1)
    return fig

