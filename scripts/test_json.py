"""_summary_
"""
import json
#import dash
#from dash import dcc, html
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
    #colorscale='<COLORSCALE>',  # Replace with the colorscale name
    colorbar=dict(title='stuff')  # Replace with your colorbar title
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
    paper_bgcolor="LightSteelBlue",
)
fig.show()

