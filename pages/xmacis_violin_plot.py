"""
This is a simple example of a Dash app that uses the ACIS API to get temperature data
for a station and then displays a violin plot comparing the temperatures for a range.
"""

from datetime import datetime
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
import plotly.graph_objects as go
import pandas as pd
import requests
import numpy as np

META_URL = "http://data.rcc-acis.org/StnMeta"
PARMS_URL = "http://data.rcc-acis.org/StnData?params="

dash.register_page(__name__,
    path='/xmacis_violin_plot',
    title='XMACIS',
    name='XMACIS',
    order=2)

mon = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug',
       9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
months = list(np.arange(1,13))
dates = list(np.arange(1,32))
month_categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                    'Oct', 'Nov', 'Dec']
columns = ['mint', 'maxt', 'avgt', 'maxt_n','mint_n','avgt_n']
dftypes = {"dts": 'string', "year": 'int', "month": 'int', "day": 'int',
           "maxt": 'int', "mint": 'int', "avgt": 'float',
           "maxt_n": 'float', "mint_n": 'float', "avgt_n": 'float'}


class XMACIS():
    """
    Class to get and store data from the ACIS API
    """
    def __init__(self, station):
        self.station = station
        self.get_por_metadata()
        self.df = self.get_all_por_data()
        self.melted = pd.melt(self.df, id_vars=['year','month','day'], \
            value_vars=columns, value_name='temperature')
        self.melted = self.melted.astype({"variable": 'string'}, errors='ignore')

    def get_por_metadata(self) -> None:
        """
        Get the metadata for the station of interest
        """
        params = {"sids": self.station, "elems": "maxt", "meta": ["name","valid_daterange"]}
        req = requests.post(META_URL, json=params, timeout=5)
        data = req.json()
        meta = data['meta'][0]
        self.full_name = meta['name']
        self.por_start_date_str = meta['valid_daterange'][0][0]
        self.por_end_date_str = meta['valid_daterange'][0][1]
        self.por_start_date_obj = datetime.strptime(self.por_start_date_str, '%Y-%m-%d')
        self.por_end_date_obj = datetime.strptime(self.por_end_date_str, '%Y-%m-%d')

    def get_all_por_data(self) -> pd.DataFrame:
        """
        Get all the data for the station of interest
        """
        parms = {
            "sid": self.station,
            "sdate": self.por_start_date_str,
            "edate": self.por_end_date_str,
            "elems": [
                {"name": "maxt", "interval": "dly", "duration": "dly"},
                {"name": "mint", "interval": "dly", "duration": "dly"},
                {"name": "avgt", "interval": "dly", "duration": "dly"},
                {"name": "maxt", "interval": "dly", "duration": "dly", "normal": "1"},
                {"name": "mint", "interval": "dly", "duration": "dly", "normal": "1"},
                {"name": "avgt", "interval": "dly", "duration": "dly", "normal": "1"},
            ]
        }
        req = requests.post(PARMS_URL, json=parms, timeout=5)
        data = req.json()
        df_init = pd.json_normalize(data)
        df_dp = df_init["data"].apply(pd.Series).T
        df = df_dp[0].apply(pd.Series)
        df.columns = ['dts', 'maxt', 'mint', 'avgt', 'maxt_n', 'mint_n', 'avgt_n']
        df['date'] = pd.to_datetime(df['dts'], errors='coerce')
        df.set_index('date', inplace=True)
        df['year'] = df.index.year
        df['month'] = df.index.month
        df['day'] = df.index.day
        df = df.astype(dftypes, errors='ignore')
        return df

# Initial setup
STATION = "GRRthr"  # Example station name
test = XMACIS(STATION)
dff = test.melted
por_start = test.por_start_date_obj.year
por_end = test.por_end_date_obj.year
yrs = list(range(por_start, por_end + 1))
dff = dff.astype({"variable": 'string'}, errors='ignore')
dff['mon'] = dff['month'].map(mon)


title = dbc.Container([
        html.Br(),
        dbc.Row([dbc.Col(html.H2("XMACIS temperatures for GRR"), width=12)])
    ])

stuff = dbc.Container([
    dbc.Row(html.Hr()),
    dbc.Row([
        dbc.Col([
            html.H6(' '),
        ], width=2),
        dbc.Col([
            html.H6('Select range of years to compare against'),
        ], width=4),
        dbc.Col([
            html.H6('Select range of years to investigate'),
        ], width=4),

    ]),
    dbc.Row(html.Hr()),
    dbc.Row([
        dbc.Col([
            html.H6('Choose element'),
            dcc.Dropdown(
                options=[
                    {'label': 'Min Temp', 'value': 'mint'},
                    {'label': 'Max Temp', 'value': 'maxt'},
                    {'label': 'Avg Temp', 'value': 'avgt'}
                ],
                value='maxt', id="element", clearable=False
            )
        ], width=2),
        dbc.Col([
            html.H6('Baseline start year'),
            dcc.Dropdown(yrs, value=por_start, id='base_start', clearable=False)
        ], width=2),
        dbc.Col([
            html.H6('Baseline end year'),
            dcc.Dropdown(yrs, value=por_end, id='base_end', clearable=False)
        ], width=2),
        dbc.Col([
            html.H6('Comparison start year'),
            dcc.Dropdown(yrs, value=por_start, id='comp_start', clearable=False)
        ], width=2),
        dbc.Col([
            html.H6('Comparison end year'),
            dcc.Dropdown(yrs, value=por_end, id='comp_end', clearable=False)
        ], width=2),

    ]),
    dbc.Row(html.H6(' ')),
    dbc.Row(dcc.Graph(id="graphing"))
])

layout = dbc.Container([title, stuff])

def create_legend(start_year, end_year):
    """
    Create a legend for the plot. If the start and end year are the same, only
    the start year is returned.
    """
    if start_year == end_year:
        return f'{start_year}'
    return f'{start_year}-{end_year}'

@callback(
    Output("graphing", "figure"),
    Input("base_start", "value"),
    Input("base_end", "value"),
    Input("comp_start", "value"),
    Input("comp_end", "value"),
    Input("element", "value"),
)
def update_violin_chart(base_start, base_end, comp_start, comp_end, element):
    """
    Update the violin chart based on the dropdown selections
    """

    df = dff[(dff['variable'] == element)]
    df_base = df[(df['year'] >= base_start) & (df['year'] <= base_end)]
    df_year = df[(df['year'] >= comp_start) & (df['year'] <= comp_end)]
    nice_name = 'Minimum Temperature'
    col = 'blue'
    if element == 'maxt':
        nice_name = 'Maximum Temperature'
        col = 'red'
    if element == 'avgt':
        nice_name = 'Average Temperature'
        col = 'orange'
    
    fig = go.Figure()
    this_name = create_legend(base_start, base_end)
    fig.add_trace(go.Violin(x=df_base['mon'], y=df_base['temperature'],
                            legendgroup='Yes', scalegroup='Yes', name=this_name,
                            side='negative',
                            line_color='gray')
                )
    this_name = create_legend(comp_start, comp_end)
    fig.add_trace(go.Violin(x=df_year['mon'],
                            y=df_year['temperature'],
                            legendgroup='No', scalegroup='No', name=this_name,
                            side='positive',
                            line_color=col)
                )
    fig.update_traces(meanline_visible=True)
    fig.update_layout(violingap=0, violinmode='overlay')
    r = [-30,120]
    fig.update_yaxes(range = r)
    fig.update_xaxes(categoryorder='array', categoryarray=month_categories)
    fig.update_layout(autotypenumbers='convert types')
    fig.update_layout(title=f'{test.full_name} - {nice_name}',
                        legend_title='',
                        yaxis_title='Temperature  (F)')
    fig.update_layout(margin={'l':20, 'r':10, 't':60, 'b':20})
    return fig



@callback(
    Output('base_end', 'options'),
    Output('base_end', 'value'),
    Input('base_start', 'value'),
    
)
def update_base_end_year_dropdown(base_start):
    """
    Updates the day dropdown based on the selected year and month
    """  
    base_end_year_list = list(range(base_start, por_end + 1))
    base_end_value = min(base_start + 30, por_end)
    return base_end_year_list, base_end_value

@callback(
    Output('comp_end', 'options'),
    Output('comp_end', 'value'),
    Input('comp_start', 'value'),
)
def update_compare_end_year_dropdown(comp_start):
    """
    Updates the day dropdown based on the selected year and month
    """
    comp_end_year_list = list(range(comp_start, por_end + 1))
    comp_end_value = min(comp_start + 30, por_end)
    return comp_end_year_list, comp_end_value
