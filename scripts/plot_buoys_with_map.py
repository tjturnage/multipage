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

# dash.register_page(__name__,
#     path='/buoymap',
#     title='Buoy Map',
#     name='Buoy Map',
#     order=8)


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
        rows=7, cols=3,
        #shared_xaxes=True,
        vertical_spacing=0.05,
        horizontal_spacing=0.03,
        specs=
        #row_heights=[0.2,0.2,0.2,0.2,0.2,0.2,0.2],
        #subplot_titles=SUBPLOT_TITLES)
    elements = ['WVHT','WSPD','GST']
    for buoy, element in itertools.product(BUOY_IDS, elements):
        buoy_dataframe = new_buoy_data[buoy]
        buoy_element = buoy_dataframe[element]
        buoy_title = BUOY_DICT[buoy]['title']
        #buoy_color = BUOY_DICT[buoy]['color']
scripts/plot_buoys_with_map .py
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
    fig.add_trace(go.Scatter, row=1, col=3, rowspan=7)
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

"""
  
# Load custom JSON map overlay data
json_url = 'C:/data/scripts/pyany/data/coastalcounties.geojson'
with open(json_url, encoding='utf-8') as json_file:
    overlay_data = json.load(json_file)

LATITUDE_VALUES = [42.0, 43.0, 43.5]
LONGITUDE_VALUES = [-86.0, -86.5, -87.0]
TEXT_VALUES = ['<b>Text 1</b>', '<b>Text 2</b>', '<b>Text 3</b>']

MAPBOX_TOKEN = 'pk.eyJ1IjoidGp0dXJuYWdlIiwiYSI6ImNsaXoydWQ1OTAyZmYzZmxsM21waWU2N3kifQ.MDNAdaS61MNNmHimdrV7Kg'

trace = go.Choroplethmapbox(
    geojson=overlay_data,
    locations=['COUNTYNAME'],  # Replace with your location values
    featureidkey='properties.FIPS',
    #colorscale='<COLORSCALE>',  # Replace with the colorscale name

)

layout = go.Layout(
    mapbox=dict(
        accesstoken=MAPBOX_TOKEN,
        style='mapbox://styles/mapbox/dark-v10',
        #center=dict(lat=43.0, lon=-86.5),  # Replace with the center coordinates
        bounds=dict(east=-85.5, west=-88.0, north=44.5, south=41.5),  # Replace with the map bounds
        zoom=7  # Replace with the desired zoom level
    ),
    margin=dict(l=0, r=0, t=0, b=0)
)

fig = go.Figure(data=[trace], layout=layout)
fig.update_traces(name='trace', selector=dict(type='choroplethmapbox'))
fig.update_layout(
    autosize=False,
    width=300,
    height=700,
    margin=dict(
        l=10,
        r=10,
        b=10,
        t=10,
        pad=4
    ),
    paper_bgcolor="LightSteelBlue",)

"""
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create a figure with subplots
fig = make_subplots(rows=7, cols=3, specs=[[{'type': 'scatter'}, {'type': 'scatter'}, {'type': 'scattermapbox'}]] * 7)

# Add scatter plots to the first two columns
for row in range(1, 8):
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[row, row, row], mode='markers'), row=row, col=1)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[row, row, row], mode='markers'), row=row, col=2)

# Add Mapbox plot to the right column
#fig.add_trace(go.Scattermapbox(
    #lat=[<LATITUDE_VALUES>],  # Replace with your latitude data
    #lon=[<LONGITUDE_VALUES>],  # Replace with your longitude data
    #mode='markers',
    #marker={'size': 10, 'color': 'red'},
    #text=[<TEXT_VALUES>]  # Replace with your text data
#), row=1, col=3, rowspan=7)

# Update layout specifications for the Mapbox plot
fig.update_layout(mapbox=dict(
        accesstoken=MAPBOX_TOKEN,
        style='mapbox://styles/mapbox/dark-v10',
        #center=dict(lat=43.0, lon=-86.5),  # Replace with the center coordinates
        bounds=dict(east=-85.5, west=-88.0, north=44.5, south=41.5),  # Replace with the map bounds
        zoom=7),
        row=1, col=3, rowspan=7)

# Show the figure
fig.show()