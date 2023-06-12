"""
This runs the buoys plot
"""
#from pathlib import Path
from datetime import datetime
import itertools
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#from . import ids
#from .side_bar import sidebar
from config import BUOY_DICT, CMAN_DICT, STYLE_DICT, BUOY_IDS, BUOY_TITLES
from config import METERS_PER_SECOND_TO_KNOTS, METERS_TO_FEET
from config import DATA_DIRECTORY
from config import update_buoys, update_times


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
def get_current_time(n):
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
    fig.update_traces(textposition='top right')
    return fig

