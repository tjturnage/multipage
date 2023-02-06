"""
Main projects page is the graffitti page
"""
from pathlib import Path
import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import geopandas as gpd
from datetime import datetime
#import pandas as pd
#from . import ids
from .side_bar import sidebar


#p = Path('/home/tjturnage')
p = Path('C:/data/scripts')
q = p / 'multipage' / 'data' / 'final_frame.geojson'

if q.exists():
    DATA = q
else:
    DATA = "../data/final_frame.geojson"

SBW = gpd.read_file(DATA,driver='GeoJSON',crs='EPSG:4326')
dts_string = list(SBW.INIT_ISS)
dts_list = []
for x in dts_string:
  dts = datetime.strptime(x,'%Y%m%d%H%M')
  dts_list.append(dts)

SBW['dts'] = dts_list
SBW_new = SBW.set_index('dts')
fixed = SBW_new.drop('INIT_ISS', axis=1)

SBW_sliced = fixed[(fixed.PHENOM == 'SV') & (fixed.index.month >= 11)]
SBW_sliced.plot(facecolor=(1, 0, 0, 0.040), edgecolor='#00000000')

dash.register_page(__name__, title="Polygons", order=1)

def layout():
    """
    Temp layout
    """
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col([sidebar()], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),
                    dbc.Col(
                        [
                            html.H3(
                                "Graffiti Incidents in Berlin",
                                style={"textAlign": "center"},
                            ),
                            dcc.Dropdown(
                                id = phenom-type,
                                options=SBW["PHENOM"].unique(),
                                value=["SV"],
                                multi=True,
                                style={"color": "black"},
                            ),
                            html.Hr(),
                            dcc.Graph(id=polygons, figure={}),
                        ],
                        xs=8,
                        sm=8,
                        md=10,
                        lg=10,
                        xl=10,
                        xxl=10,
                    ),
                ]
            )
        ]
    )
