"""
This runs the buoys plot
"""
#from pathlib import Path
from datetime import datetime, timedelta
import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
#from . import ids
#from .side_bar import sidebar


dash.register_page(__name__,
    path='/buoys',
    title='Buoy Observations',
    name='Buoys',
    order=6)

column_master_list = []
ELEMENT_NAMES = ['WDIR','WSPD','WGST','WVHT']
ELEMENT_DICT = {'WDIR': 0, 'WSPD': 1, 'WGST': 2, 'WVHT': 3}
METERS_PER_SECOND_TO_KNOTS = 1.94384
METERS_TO_FEET = 3.280
BASE_URL = 'https://www.ndbc.noaa.gov/data/realtime2'

BUOY_NAMES = {'45024': 'Ludington Buoy',
         'LDTM4': 'Ludington',
         '45161': 'Muskegon Buoy',
         'MKGM4': 'Muskegon',
         '45029': 'Holland Buoy',
         'HLNM4': 'Holland',
         '45168': 'South Haven Buoy',
         'SVNM4': 'South Haven',
         '45007': 'LM South Buoy'
}

BUOYS = list(BUOY_NAMES.keys())

df_45024 = pd.DataFrame()
df_LDTM4 = pd.DataFrame()
df_45161 = pd.DataFrame()
df_MKGM4 = pd.DataFrame()
df_45029 = pd.DataFrame()
df_HLNM4 = pd.DataFrame()
df_45168 = pd.DataFrame()
df_SVNM4 = pd.DataFrame()
df_45007 = pd.DataFrame()

buoy_dataframes = {'45024': df_45024,
                   'LDTM4': df_LDTM4,
                   '45161': df_45161,
                   'MKGM4': df_MKGM4,
                   '45029': df_45029,
                   'HLNM4': df_HLNM4,
                   '45168': df_45168,
                   'SVNM4': df_SVNM4,
                   '45007': df_45007
                   }

for buoy in BUOYS:
    df = buoy_dataframes[buoy]
    url = f'{BASE_URL}/{buoy}.txt'
    df = pd.read_csv(url, delim_whitespace=True, skiprows=[1], na_values='MM', nrows=200)
    column_names = df.columns.tolist()
    column_mapping = {'#YY': 'year', 'MM': 'month', 'DD': 'day', 'hh': 'hour', 'mm': 'minute'}
    df = df.rename(columns=column_mapping)

    df = df.iloc[:, :-10]
    df['datetime'] = pd.to_datetime(df[['year','month','day','hour','minute']])
    df.drop(columns=['year','month','day','hour','minute'], inplace=True)
    df['WSPD'] = df['WSPD'] * METERS_PER_SECOND_TO_KNOTS
    df['GST'] = df['GST'] * METERS_PER_SECOND_TO_KNOTS
    df['WVHT'] = df['WVHT'] * METERS_TO_FEET

  # copy this freshly made dataframe to the specific df for this site
    buoy_dataframes[buoy] = df.copy(deep=True)


def layout():
    """
    This defines the dashboard
    """
    return html.Div([
        dbc.Container([
            dbc.Row(dbc.Col([html.H2("Buoy Observations")])),
            dbc.Row(dbc.Col(dcc.Dropdown(BUOYS, BUOYS[0], id='dropdown'))),
            dbc.Row(dbc.Col(dcc.Graph(id='buoy_graph')))
        ])
    ])


@callback(
    Output(component_id = 'buoy_graph', component_property = 'figure'),
    Input(component_id = 'dropdown', component_property = 'value'), suppress_callback_exceptions=True)
def update_graph(buoy):
    """
    This updates the graph
    """
    now = datetime.utcnow()
    start = now - timedelta(hours=6)
    this_df = buoy_dataframes[buoy]
    df_short = this_df.loc[this_df['datetime'] > start]
    if df_short['WVHT'].max() > 10:
        max_wave = 15
    elif df_short['WVHT'].max() > 5:
        max_wave = 10
    elif df_short['WVHT'].max() > 3:
        max_wave = 5
    else:
        max_wave = 3
    fig = px.line(df_short, x='datetime', y='WVHT', range_y=[0, max_wave], title=f'{buoy} - {BUOY_NAMES[buoy]}')
    return fig
