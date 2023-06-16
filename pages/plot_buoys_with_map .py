"""
This runs the buoys plot
"""
from datetime import datetime
import itertools
import pandas as pd
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from config import BUOY_DICT, SUBPLOT_TITLES, BUOY_IDS
from config import update_buoys, update_times

from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

dash.register_page(__name__,
    path='/buoymap',
    title='Buoy Map',
    name='Buoy Map',
    order=8)


def layout():
    """_summary_

    Returns:
        _type_: _description_
    """
    return html.Div(
        dbc.Container([
            dbc.Row([
                dbc.Col([                
                    dbc.Row(dbc.Col(html.H2("Buoy Observations"))),
                    dbc.Row(dbc.Col(html.H5(id='series-time'))),
                    dbc.Row(dbc.Col(dcc.Graph(id='series-graph'))),
                    dcc.Interval(
                        id='map-interval',
                        interval=5 * 60 * 1000,  # in milliseconds
                        n_intervals=0,
                        max_intervals=-1)
                ]),
                dbc.Col([
                    dbc.Row(dbc.Col(html.H2("Buoy Observations"))),
                    dbc.Row(dbc.Col(html.H5(id='map-time'))),
                    dbc.Row(dbc.Col(dcc.Graph(figure={},id='map-graph'))),
                    ]),
                ])
            ])
        )
    

@dash.callback(Output(component_id = 'series-time', component_property = 'children'),
          Input(component_id = 'map-interval', component_property = 'n_intervals'))
def get_current_time(_n):
    """
    Returns the current time in UTC
    Args:
        n: int : interval input that activates callback
        
    Returns:
        datetime string
    """
    return f'Updated:  {datetime.utcnow().strftime(" %H:%M UTC -- %b %d, %Y")}'

@dash.callback(Output('series-graph', 'figure'),
          Input('map-interval', 'n_intervals'))
def update_series_plots(_n):
    """_summary_

    Args:
        n: int : interval input that activates callback (unused)

    Returns:
        fig: figure
    """
    now,start_time,end_time = update_times()
    new_buoy_data, max_wave, min_wave, max_speed, min_speed = update_buoys()
    fig = make_subplots(
        rows=7, cols=2,
        shared_xaxes=True,
        vertical_spacing=0.05,
        horizontal_spacing=0.03,
        row_heights=[0.2,0.2,0.2,0.2,0.2,0.2,0.2],
        subplot_titles=SUBPLOT_TITLES)
    elements = ['WVHT','WSPD','GST']
    for buoy, element in itertools.product(BUOY_IDS, elements):
        buoy_dataframe = new_buoy_data[buoy]
        buoy_element = buoy_dataframe[element]
        buoy_title = BUOY_DICT[buoy]['title']
        #buoy_color = BUOY_DICT[buoy]['color']
        row = BUOY_DICT[buoy]['row']
        this_line_dict = {}
        this_line_dict['color'] = 'rgba(255, 255, 255, 1)'
        this_line_dict['width'] = 3.5
        this_line_dict['dash'] = 'solid'
        if element == 'WVHT':
            fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, text=buoy_title, line=this_line_dict, hovertemplate = '%{y:.2f} ft'), row=row, col=1)   
        if element == 'WSPD':
            this_marker_dict=dict(color=this_line_dict['color'], size=7)
            #fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, text=buoy_title, line=this_line_dict, hovertemplate = '%{y:.0f} kt'), row=row, col=2)
            fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, mode="markers", marker=this_marker_dict, hovertemplate = '%{y:.0f} kt'), row=row, col=2)
        if element == 'GST':
            grayish = "rgba(215, 215, 215, 1)"
            this_line_dict['color'] = grayish
            this_marker_dict=dict(color=this_line_dict['color'], size=4)
            fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, mode="markers", marker=this_marker_dict, hovertemplate='G %{y:.0f} kt'), row=row, col=2)
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

    fig.update_layout(template='plotly_dark')
    wind_range = dict(range=[min_speed, max_speed])
    wave_range = dict(range=[min_wave, max_wave])
    fig.update_layout(yaxis1 = wave_range)
    fig.update_layout(yaxis2 = wind_range)
    fig.update_layout(hovermode="x unified")
    fig.update_layout(title_x=0.08)

    greenish = "rgba(0, 128, 0, 0.55)"
    yellowish = "rgba(180, 180, 0, 0.45)"
    orangish = "rgba(255, 119, 0, 0.5)"
    reddish = "rgba(200, 0, 0, 0.5)"
    #reddish = "rgba(200, 0, 0, 1)"
    #speed_yellow = [22,33.5] # SCA
    #speed_orange = [33.5,47.5] # Gale
    #speed_red = [47.5,60] # storm
    for r in range(1,8):
        fig.add_hrect(y0=min_wave, y1=3.5, fillcolor=greenish, line_width=0, row=r, col=1)
        fig.add_hrect(y0=3.5, y1=100, fillcolor=yellowish, line_width=0, row=r, col=1)
    
        fig.add_hrect(y0=min_speed, y1=min(max_speed,21.5), fillcolor=greenish, line_width=0, row=r, col=2)
        if max_speed > 21.5:
            fig.add_hrect(y0=21.5, y1=min(max_speed,33.5), fillcolor=yellowish, line_width=0, row=r, col=2)
        if max_speed > 33.5:
            fig.add_hrect(y0=33.5, y1=min(max_speed,47.5), fillcolor=orangish, line_width=0, row=r, col=2)
        if max_speed > 47.5:
            fig.add_hrect(y0=47.5, y1=min(max_speed,63), fillcolor="pink", opacity=1, line_width=0, row=r, col=2)
    #fig.add_hline(y=22, line=dict(dash="solid", width=2, color=danger), row=2, col=1)
        fig.add_vline(x=now, line=dict(dash="solid", width=2, color='white'), row=r, col=1)
        fig.add_vline(x=now, line=dict(dash="solid", width=2, color='white'), row=r, col=2)

    wave_range = dict(range=[min_wave, max_wave])
    wind_range = dict(range=[min_speed, max_speed])
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
    fig.update_layout(yaxis13 = wave_range)
    fig.update_layout(yaxis14 = wind_range)
    fig.update_traces(textposition='top right')
    fig.update_shapes(layer="below")
    return fig

@dash.callback(Output('map-graph', 'figure'),
          Input('map-interval', 'n_intervals'))
def update_map(_n):
    """_summary_

    Args:
        n: int : interval input that activates callback (unused)

    Returns:
        fig: figure
    """

    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                    dtype={"fips": str})



    fig2 = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                            color_continuous_scale="Viridis",
                            range_color=(0, 12),
                            scope="usa",
                            labels={'unemp':'unemployment rate'}
                            )
    fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig2

