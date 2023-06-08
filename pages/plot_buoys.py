"""
This runs the buoys plot
"""
#from pathlib import Path
from datetime import datetime, timedelta
from pathlib import Path
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
#from . import ids
#from .side_bar import sidebar

now = datetime.utcnow()
start = now - timedelta(hours=3)

#root_directory = Path().absolute().parts[0]
#scripts_directory = root_directory / 'data' / 'scripts' / 'pyany' / 'data'
read_data_directory = '/home/tjturnage/multipage/data'
if 'pyany' in Path().absolute().parts:
    read_data_directory = 'C:/data/scripts/pyany/data'


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

new_buoy_data = {}

BUOYS = list(BUOY_NAMES.keys())

max_height = 0
max_speed = 0

for buoy in BUOYS:
    buoy_dataframe = None
    source = f'{read_data_directory}/{buoy}.csv'
    buoy_dataframe = pd.read_csv(source, parse_dates=['dts'], index_col='dts')
    max_height = max(max_height, buoy_dataframe['WVHT'].max())
    max_speed = max(max_speed, buoy_dataframe['GST'].max())
    new_buoy_data[buoy] = buoy_dataframe

dash.register_page(__name__,
    path='/buoys2',
    title='Buoys',
    name='Buoys',
    order=8)



def layout():
    return html.Div([
        dbc.Container([
            dbc.Row(dbc.Col(html.H2("Buoy Observations"))),
            dbc.Row(dbc.Col(dcc.Graph(id='graph', figure=fig)))
        ]),

    ])


if max_height > 15:
    max_wave = 20
elif max_height > 10:
    max_wave = 15
elif max_height > 5:
    max_wave = 10
else:
    max_wave = 5
marker_dict = dict(color='white', size=3)
#y = list(this_df['GST'])
#marker_dict = dict(list(map(set_color, y)))
wave_line_dict = dict(color='#00CCCC', width=3)
wind_line_dict = dict(color='gray', width=3)
#wind_hover = "<b>%{text}</b><br><br>GDP per Capita: %{x:$,.0f}<br>%{y:.0%}<br><extra></extra>"

wspd_title = 'Wind Speed and Gust (kt)'

fig = make_subplots(
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
fig.add_trace(go.Scatter(x=new_buoy_data['45024'].index, y=new_buoy_data['45024']['WVHT'], name='Ludington', line=wave_line_dict), row=1, col=1)
fig.add_trace(go.Scatter(x=new_buoy_data['45161'].index, y=new_buoy_data['45161']['WVHT'], name='Muskegon', line=wave_line_dict), row=2, col=1)
fig.add_trace(go.Scatter(x=new_buoy_data['45029'].index, y=new_buoy_data['45029']['WVHT'], name='Holland', line=wave_line_dict), row=3, col=1)
fig.add_trace(go.Scatter(x=new_buoy_data['45168'].index, y=new_buoy_data['45168']['WVHT'], name='South Haven', line=wave_line_dict), row=4, col=1)
fig.add_trace(go.Scatter(x=new_buoy_data['45210'].index, y=new_buoy_data['45210']['WVHT'], name='Central LM',  line=wave_line_dict), row=5, col=1)
fig.add_trace(go.Scatter(x=new_buoy_data['45007'].index, y=new_buoy_data['45007']['WVHT'], name='South LM',  line=wave_line_dict), row=6, col=1)
fig.update_xaxes(range=[start, now])
fig.update_yaxes(range=[0, max_wave])
fig.update_xaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
fig.update_yaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
fig.update_layout(showlegend=False)


#fig2 = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.06, horizontal_spacing=0.01,row_heights=[0.25,0.25,0.25,0.25])
fig.add_trace(go.Scatter(x=new_buoy_data['45024'].index, y=new_buoy_data['45024']['WSPD'], name='Ludington', line=wind_line_dict), row=1, col=2)
fig.add_trace(go.Scatter(x=new_buoy_data['45024'].index, y=new_buoy_data['45024']['GST'], mode='markers', name='Ludington', marker=marker_dict), row=1, col=2)

fig.add_trace(go.Scatter(x=new_buoy_data['45161'].index, y=new_buoy_data['45161']['WSPD'], name='Muskegon', line=wind_line_dict), row=2, col=2)
fig.add_trace(go.Scatter(x=new_buoy_data['45161'].index, y=new_buoy_data['45161']['GST'], mode='markers', name='Muskegon', marker=marker_dict), row=2, col=2)

fig.add_trace(go.Scatter(x=new_buoy_data['45029'].index, y=new_buoy_data['45029']['WSPD'], name='Holland', line=wind_line_dict), row=3, col=2)
fig.add_trace(go.Scatter(x=new_buoy_data['45029'].index, y=new_buoy_data['45029']['GST'], mode='markers', name='Holland', marker=marker_dict), row=3, col=2)

fig.add_trace(go.Scatter(x=new_buoy_data['45168'].index, y=new_buoy_data['45168']['WSPD'], name='South Haven', line=wind_line_dict), row=4, col=2)
fig.add_trace(go.Scatter(x=new_buoy_data['45168'].index, y=new_buoy_data['45168']['GST'], mode='markers', name='South Haven', marker=marker_dict), row=4, col=2)

fig.add_trace(go.Scatter(x=new_buoy_data['45210'].index, y=new_buoy_data['45210']['WSPD'], name='Central LM', line=wind_line_dict), row=5, col=2)

fig.add_trace(go.Scatter(x=new_buoy_data['45007'].index, y=new_buoy_data['45007']['WSPD'], name='South LM', line=wind_line_dict), row=6, col=2)
fig.add_trace(go.Scatter(x=new_buoy_data['45007'].index, y=new_buoy_data['45007']['GST'], mode='markers', name='South LM', marker=marker_dict), row=6, col=2)
fig.update_xaxes(range=[start, now])
fig.update_yaxes(range=[0, max_speed])
fig.update_xaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
fig.update_yaxes(showline=True, linewidth=1, linecolor='gray', mirror=True)
fig.update_layout(showlegend=False)
fig.update_layout(
    autosize=False,
    width=1200,
    height=800,
    margin=dict(
        l=10,
        r=10,
        b=10,
        t=40,
        pad=4
    )
)

fig.update_layout(template='plotly_dark')
#fig2.update_layout(template='plotly_dark')
wave_range = dict(range=[0,max_wave])
wind_range = dict(range=[0, max_speed])
#fig.update_layout(height=800, width=600, title_text="Wave Height (ft)")
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
fig.update_layout(hovermode="x unified")
fig.update_layout(title_x=0.01)

