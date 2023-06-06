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
         '45210': 'Central LM',
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
df_45210 = pd.DataFrame()
df_45007 = pd.DataFrame()

buoy_data = {'45024': df_45024,
                'LDTM4': df_ldtm4,
                '45161': df_45161,
                'MKGM4': df_mkgm4,
                '45029': df_45029,
                'HLNM4': df_hlnm4,
                '45168': df_45168,
                'SVNM4': df_svnm4,
                '45210': df_45210,
                '45007': df_45007
                }
now = datetime.utcnow()
start = now - timedelta(hours=3)

max_waveheight = 0
max_windspeed = 0

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
    max_windspeed = max(max_windspeed, short_df['GST'].max())
# copy this freshly made dataframe to the specific df for this site
    buoy_data[buoy] = short_df.copy(deep=True)


dash.register_page(__name__,
    path='/buoys',
    title='Buoy Observations',
    name='Buoys',
    order=6)

"""
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
app.layout = html.Div([
        dbc.Container([
            #dbc.Row(dbc.Col(html.H2("Buoy Observations"))),
            dbc.Row([dbc.Col(html.H3("WaveHeight")),dbc.Col(html.H3("Windspeed"))]),
            dbc.Row(dbc.Col(dcc.Graph(id='buoy_graph', figure=fig1)))
        ]),
        dcc.Interval(
            id='interval-component',
            interval=10*1000, # in milliseconds
            n_intervals=0
        )
    ])
"""

def layout():
    """
    This defines the dashboard
    """
    return html.Div([
        dbc.Container([
            #dbc.Row(dbc.Col(html.H2("Buoy Observations"))),
            dbc.Row(dbc.Col(dcc.Graph(id='buoy_graph', figure=fig1)))
        ])
    ])

if max_waveheight > 15:
    max_wave = 20
elif max_waveheight > 10:
    max_wave = 15
elif max_waveheight > 5:
    max_wave = 10
else:
    max_wave = 5
    

marker_dict = dict(color='white', size=3)
line_dict = dict(color='gray', width=3)
wave_line_dict = dict(color='#00CCCC', width=3)
wind_line_dict = dict(color='gray', width=3)
wind_hover = "<b>%{text}</b><br><br>GDP per Capita: %{x:$,.0f}<br>%{y:.0%}<br><extra></extra>"

wspd_title = 'Wind Speed and Gust (kt)'

fig1 = make_subplots(
    rows=6, cols=2,
    shared_xaxes=True,
    vertical_spacing=0.05,
    horizontal_spacing=0.04,
    row_heights=[0.25,0.25,0.25,0.25,0.25,0.25],
    subplot_titles=('<b><span style="color:#DDDD33;">Ludington</span></b> Wave Height (ft)', wspd_title,
                    '<b><span style="color:#DDDD33;">Muskegon</span></b> Wave Height (ft)', wspd_title,
                    '<b><span style="color:#DDDD33;">Holland</span></b> Wave Height (ft)', wspd_title,
                    '<b><span style="color:#DDDD33;">South Haven</span></b> Wave Height (ft)', wspd_title,
                    '<b><span style="color:#DDDD33;">Central LM</span></b> Wave Height (ft)', wspd_title,
                    '<b><span style="color:#DDDD33;">South LM</span></b> Wave Height (ft)', wspd_title))
fig1.add_trace(go.Scatter(x=buoy_data['45024']['dts'], y=buoy_data['45024']['WVHT'], name='Ludington', line=wave_line_dict), row=1, col=1)
fig1.add_trace(go.Scatter(x=buoy_data['45161']['dts'], y=buoy_data['45161']['WVHT'], name='Muskegon', line=wave_line_dict), row=2, col=1)
fig1.add_trace(go.Scatter(x=buoy_data['45029']['dts'], y=buoy_data['45029']['WVHT'], name='Holland', line=wave_line_dict), row=3, col=1)
fig1.add_trace(go.Scatter(x=buoy_data['45168']['dts'], y=buoy_data['45168']['WVHT'], name='South Haven', line=wave_line_dict), row=4, col=1)
fig1.add_trace(go.Scatter(x=buoy_data['45210']['dts'], y=buoy_data['45210']['WVHT'], name='Central LM',  line=wave_line_dict), row=5, col=1)
fig1.add_trace(go.Scatter(x=buoy_data['45007']['dts'], y=buoy_data['45007']['WVHT'], name='South LM',  line=wave_line_dict), row=6, col=1)
fig1.update_xaxes(range=[start, now])
fig1.update_yaxes(range=[0,max_wave])
fig1.update_xaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
fig1.update_yaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
fig1.update_layout(showlegend=False)


#fig2 = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.06, horizontal_spacing=0.01,row_heights=[0.25,0.25,0.25,0.25])
fig1.add_trace(go.Scatter(x=buoy_data['45024']['dts'], y=buoy_data['45024']['WSPD'], name='Ludington', line=line_dict), row=1, col=2)
fig1.add_trace(go.Scatter(x=buoy_data['45024']['dts'], y=buoy_data['45024']['GST'], mode='markers', name='Ludington', marker=marker_dict), row=1, col=2)

fig1.add_trace(go.Scatter(x=buoy_data['45161']['dts'], y=buoy_data['45161']['WSPD'], name='Muskegon', line=line_dict), row=2, col=2)
fig1.add_trace(go.Scatter(x=buoy_data['45161']['dts'], y=buoy_data['45161']['GST'], mode='markers', name='Muskegon', marker=marker_dict), row=2, col=2)

fig1.add_trace(go.Scatter(x=buoy_data['45029']['dts'], y=buoy_data['45029']['WSPD'], name='Holland', line=line_dict), row=3, col=2)
fig1.add_trace(go.Scatter(x=buoy_data['45029']['dts'], y=buoy_data['45029']['GST'], mode='markers', name='Holland', marker=marker_dict), row=3, col=2)

fig1.add_trace(go.Scatter(x=buoy_data['45168']['dts'], y=buoy_data['45168']['WSPD'], name='South Haven', line=line_dict), row=4, col=2)
fig1.add_trace(go.Scatter(x=buoy_data['45168']['dts'], y=buoy_data['45168']['GST'], mode='markers', name='South Haven', marker=marker_dict), row=4, col=2)

fig1.add_trace(go.Scatter(x=buoy_data['45210']['dts'], y=buoy_data['45210']['WSPD'], name='Central LM', line=line_dict), row=5, col=2)

fig1.add_trace(go.Scatter(x=buoy_data['45007']['dts'], y=buoy_data['45007']['WSPD'], name='South LM', line=line_dict), row=6, col=2)
fig1.add_trace(go.Scatter(x=buoy_data['45007']['dts'], y=buoy_data['45007']['GST'], mode='markers', name='South LM', marker=marker_dict), row=6, col=2)
fig1.update_xaxes(range=[start, now])
fig1.update_yaxes(range=[0,max_windspeed])
fig1.update_xaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
fig1.update_yaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
fig1.update_layout(showlegend=False)
fig1.update_layout(
    autosize=False,
    width=1000,
    height=800,
    margin=dict(
        l=10,
        r=10,
        b=10,
        t=25,
        pad=4
    )
)

fig1.update_layout(template='plotly_dark')
#fig2.update_layout(template='plotly_dark')
wave_range = dict(range=[0,max_wave])
wind_range = dict(range=[0,max_windspeed])
#fig1.update_layout(height=800, width=600, title_text="Wave Height (ft)")
fig1.update_layout(yaxis1 = wave_range)
fig1.update_layout(yaxis2 = wind_range)
fig1.update_layout(yaxis3 = wave_range)
fig1.update_layout(yaxis4 = wind_range)
fig1.update_layout(yaxis5 = wave_range)
fig1.update_layout(yaxis6 = wind_range)
fig1.update_layout(yaxis7 = wave_range)
fig1.update_layout(yaxis8 = wind_range)
fig1.update_layout(yaxis9 = wave_range)
fig1.update_layout(yaxis10 = wind_range)
fig1.update_layout(yaxis11 = wave_range)
fig1.update_layout(yaxis12 = wind_range)
fig1.update_layout(hovermode="x unified")
fig1.update_layout(title_x=0.01)

