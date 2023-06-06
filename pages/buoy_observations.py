"""
This runs the buoys plot
"""
#from pathlib import Path
from datetime import datetime, timedelta
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
#from . import ids
#from .side_bar import sidebar


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
df_ldtm4 = pd.DataFrame()
df_45161 = pd.DataFrame()
df_mkgm4 = pd.DataFrame()
df_45029 = pd.DataFrame()
df_hlnm4 = pd.DataFrame()
df_45168 = pd.DataFrame()
df_svnm4 = pd.DataFrame()
df_45007 = pd.DataFrame()

buoy_data = {'45024': df_45024,
                'LDTM4': df_ldtm4,
                '45161': df_45161,
                'MKGM4': df_mkgm4,
                '45029': df_45029,
                'HLNM4': df_hlnm4,
                '45168': df_45168,
                'SVNM4': df_svnm4,
                '45007': df_45007
                }
now = datetime.utcnow()
start = now - timedelta(hours=10)

max_waveheight = 0

for buoy in BUOYS:
    this_df = buoy_data[buoy]
    url = f'{BASE_URL}/{buoy}.txt'
    this_df = pd.read_csv(url, delim_whitespace=True, skiprows=[1], na_values='MM', nrows=200)

    column_mapping = {'#YY': 'year', 'MM': 'month', 'DD': 'day', 'hh': 'hour', 'mm': 'minute'}
    this_df = this_df.rename(columns=column_mapping)

    this_df = this_df.iloc[:, :-10]
    this_df['dts'] = pd.to_datetime(this_df[['year','month','day','hour','minute']])
    this_df.drop(columns=['year','month','day','hour','minute'], inplace=True)
    this_df['WSPD'] = this_df['WSPD'] * METERS_PER_SECOND_TO_KNOTS
    this_df['GST'] = this_df['GST'] * METERS_PER_SECOND_TO_KNOTS
    this_df['WVHT'] = this_df['WVHT'] * METERS_TO_FEET
    short_df = this_df.loc[this_df['dts'] > start]
    max_waveheight = max(max_waveheight, short_df['WVHT'].max())

# copy this freshly made dataframe to the specific df for this site
    buoy_data[buoy] = short_df.copy(deep=True)


dash.register_page(__name__,
    path='/buoys',
    title='Buoy Observations',
    name='Buoys',
    order=6)

def layout():
    """
    This defines the dashboard
    """
    return html.Div([
        dbc.Container([
            dbc.Row(dbc.Col([html.H2("Buoy Observations")])),
            dbc.Row(dbc.Col(dcc.Graph(id='buoy_graph', figure=fig)))
        ])
    ])

if max_waveheight > 10:
    max_wave = 15
elif max_waveheight > 5:
    max_wave = 10
elif max_waveheight > 3:
    max_wave = 5
else:
    max_wave = 3

fig = make_subplots(rows=4, cols=2, shared_xaxes=True, vertical_spacing=0.03, horizontal_spacing=0.01,row_heights=[0.25,0.25,0.25,0.25])
#layout = go.Layout(
#        xaxis=dict(range=[start, now]))

print(buoy_data['45024']['WVHT'])

fig.add_trace(go.Scatter(x=buoy_data['45024']['dts'], y=buoy_data['45024']['WVHT'], name='Ludington'), row=1, col=1)
fig.add_trace(go.Scatter(x=buoy_data['45024']['dts'], y=buoy_data['45024']['WSPD'], name='Ludington'), row=1, col=2)
fig.add_trace(go.Scatter(x=buoy_data['45161']['dts'], y=buoy_data['45161']['WVHT'], name='Muskegon'), row=2, col=1)
fig.add_trace(go.Scatter(x=buoy_data['45161']['dts'], y=buoy_data['45161']['WSPD'], name='Muskegon'), row=2, col=2)
fig.add_trace(go.Scatter(x=buoy_data['45029']['dts'], y=buoy_data['45029']['WVHT'], name='Holland'), row=3, col=1)
fig.add_trace(go.Scatter(x=buoy_data['45029']['dts'], y=buoy_data['45029']['WSPD'], mode='lines+markers', name='Holland'), row=3, col=2)
fig.add_trace(go.Scatter(x=buoy_data['45029']['dts'], y=buoy_data['45029']['GST'], mode='markers', name='Holland'), row=3, col=2)
fig.add_trace(go.Scatter(x=buoy_data['45168']['dts'], y=buoy_data['45168']['WVHT'], name='South Haven'), row=4, col=1)
fig.add_trace(go.Scatter(x=buoy_data['45168']['dts'], y=buoy_data['45168']['WSPD'], name='South Haven'), row=4, col=2)
fig.update_layout(height=800, width=1200, title_text="Wave Height (ft)")
fig.update_layout(yaxis1 = dict(range=[0,max_wave]))
fig.update_layout(yaxis2 = dict(range=[0,max_wave]))
fig.update_layout(yaxis3 = dict(range=[0,max_wave]))
fig.update_layout(yaxis4 = dict(range=[0,max_wave]))
fig.update_layout(xaxis1 = dict(range=[start, now]))
fig.update_layout(xaxis2 = dict(range=[start, now]))
fig.update_layout(xaxis3 = dict(range=[start, now]))
fig.update_layout(xaxis4 = dict(range=[start, now]))
fig.update_layout(showlegend=False)
fig.update_layout(template='plotly_dark')