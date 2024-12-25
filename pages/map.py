"""
This module contains the layout for the map page of the Dash app.
"""
import os
import sys
import json
from pathlib import Path
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objects as go

from dotenv import load_dotenv
load_dotenv()
API_TOKEN = os.getenv("MAPBOX_TOKEN")

dash.register_page(__name__,
    path='/map',
    title='Map',
    name='Map',
    order=5)

if sys.platform.startswith('win'):
    p = Path('C:/data/scripts')
else:
    p = Path('/home/tjturnage')

Geojson = p / 'multipage' / 'data' / 'coastalcounties.geojson'

# Load GeoJSON data
with open(Geojson, encoding='utf-8') as f:
    geojson_data = json.load(f)

# Create the Mapbox plot
fig = go.Figure(go.Choroplethmapbox(
    geojson=geojson_data,
    locations=[feature['properties']['FIPS'] for feature in geojson_data['features']],
    z=[1] * len(geojson_data['features']),  # Dummy values for coloring
    colorscale='Viridis',
    marker_opacity=0.5,
    marker_line_width=0
))

fig.update_layout(
    mapbox=dict(
        accesstoken='API_TOKEN',  # Replace with your Mapbox access token
        center=dict(lat=41.0902, lon=-88.7129),  # Center of the United States
        zoom=5,
        style='carto-positron'
    ),
    margin={"r":0,"t":0,"l":0,"b":0}
)

layout = dbc.Container(
    dbc.Row(
        dbc.Col(
            [
                html.H1("Map of Coastal Counties in the United States"),
                dcc.Graph(figure=fig)
            ],
            width=12,
        )
    )
)