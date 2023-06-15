"""
This runs the buoys plot
"""
from datetime import datetime
import itertools
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from config import BUOY_DICT, SUBPLOT_TITLES, BUOY_IDS
from config import update_buoys, update_times

dash.register_page(__name__,
    path='/buoys',
    title='Buoys',
    name='Buoys',
    order=7)


def layout():
    """_summary_

    Returns:
        _type_: _description_
    """
    return html.Div([
        dbc.Container([
            dbc.Row(dbc.Col(html.H2("Buoy Observations"))),
            dbc.Row(dbc.Col(html.H5(id='each-time'))),
            dbc.Row(dbc.Col(dcc.Graph(id='each-graph'))),
            dcc.Interval(
                id='each-interval',
                interval=5 * 60 * 1000,  # in milliseconds
                n_intervals=0,
                max_intervals=-1)
        ]),

    ])

@dash.callback(Output('each-time', 'children'),
          Input('each-interval', 'n_intervals'))
def get_current_time(_n):
    """
    Returns the current time in UTC
    Args:
        n: int : interval input that activates callback
        
    Returns:
        datetime string
    """
    return f'Updated:  {datetime.utcnow().strftime(" %H:%M UTC -- %b %d, %Y")}'

@dash.callback(Output('each-graph', 'figure'),
          Input('each-interval', 'n_intervals'))
def update_graph(_n):
    """_summary_

    Args:
        n: int : interval input that activates callback (unused)

    Returns:
        fig: figure
    """
    now,start_time,end_time = update_times()
    new_buoy_data, max_wave, min_wave, max_speed, min_speed = update_buoys()
    fig = make_subplots(
        rows=6, cols=2,
        shared_xaxes=True,
        vertical_spacing=0.05,
        horizontal_spacing=0.03,
        row_heights=[0.2,0.2,0.2,0.2,0.2,0.2],
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
            #a = list(buoy_dataframe.index)
            #b = list(buoy_dataframe['WSPD'])
            #for c, d in zip(a, b):
            #    fig.add_annotation(x=c, y=d, text="->", showarrow=True), row=row, col=2)
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

    #fig.add_hline(y=4, line=dict(dash="solid", width=2, color=danger), row=1, col=1)
    #fig.add_hline(y=18, line=dict(dash="solid", width=2, color=caution), row=2, col=1)
    """_summary_
green is 21 knots or less and waves less than 3.5 feet
yellow is 22-33 knots and waves 3.5 feet or greater
gale is orange and winds of 34 to 47 knots
storm is red and 48 knots to 63 knots

    """
    
    greenish = "rgba(0, 128, 0, 1)"
    yellowish = "rgba(180, 180, 0, 1)"
    orangish = "rgba(255, 119, 0, 1)"
    reddish = "rgba(200, 0, 0, 1)"
    speed_yellow = [22,33.5] # SCA
    speed_orange = [33.5,47.5] # Gale
    speed_red = [47.5,60] # storm
    for r in range(1,7):
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
    fig.update_traces(textposition='top right')
    fig.update_shapes(layer="below")
    return fig

