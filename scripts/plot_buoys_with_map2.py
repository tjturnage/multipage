"""
This runs the buoys plot
"""
from pathlib import Path
from datetime import datetime, timedelta
import itertools
import pandas as pd
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from config import BUOY_DICT, SUBPLOT_TITLES, BUOY_IDS
#from config import update_buoys, update_times

from urllib.request import urlopen
import json

dash.register_page(__name__,
    path='/buoymap',
    title='Buoy Map',
    name='Buoy Map',
    order=8)


class PlotTimes:
    """_summary_

    Attributes:
        now: _type_: _description_
        hours: _type_: _description_
        minutes: _type_: _description_
        start_time: _type_: _description_
        end_time: _type_: _description_
        update_time: _type_: _description_
    """
    def __init__(self, hours=3, minutes=10):
        self.now: datetime = datetime.utcnow()
        self.hours: int = hours
        self.minutes: int = minutes
        self.start_time: datetime = self.now - timedelta(hours=self.hours)
        self.end_time: datetime = self.now + timedelta(minutes=self.minutes)
        self.update_time: str = f'Updated:  {self.now.strftime(" %H:%M UTC -- %b %d, %Y")}'


class BuoyData:
    """
    creates a dictionary of dataframes by reading a csv file
    for each buoy id in BUOY_IDS
    """
    def __init__(self) -> None:
        self.data = {}
        max_height: float = 0
        max_speed: float = 0
        min_height: float = 100
        min_speed: float = 100
        self.plot_times = PlotTimes()

    @property
    def directory(self) -> str:
        if 'pyany' in Path().absolute().parts:
            return 'C:/data/scripts/pyany/data'
        return '/home/tjturnage/multipage/data'   
    
    
    def get_buoy_data(self) -> None:
        """
        creates a dictionary of dataframes by reading a csv file
        for each buoy id in BUOY_IDS
        """
        for buoy in BUOY_IDS:
            this_source = f'{self.directory}/{buoy}.csv'
            temp_dataframe = pd.read_csv(this_source, parse_dates=['dts'], index_col='dts')
            set_ranges_df = temp_dataframe.loc[temp_dataframe.index >= self.plot_times.start_time]
            self.max_height = max(self.max_height, set_ranges_df['WVHT'].max())
            self.max_speed = max(self.max_speed, set_ranges_df['GST'].max())
            self.min_height = min(self.min_height, set_ranges_df['WVHT'].min())
            self.min_speed = min(self.min_speed, set_ranges_df['GST'].min())
            self.data[buoy] = temp_dataframe
        
        self.max_height += 1
        if self.min_height > 1:
            self.min_height -= 1

        self.max_speed = self.max_speed + 5 - (self.max_speed % 5)        
        if self.min_speed > 5:
            self.min_speed = self.min_speed - 5 + (self.min_speed % 5)
        

class PlotBuoy:

    def __init__(self) -> None:
        self.buoys = BuoyData()
        self.times = PlotTimes()
        
    def layout(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return html.Div(
        dbc.Container([
        dbc.Row([dbc.Col([html.H2("Buoy Observations")],width=12)]),
        dbc.Row([dbc.Col([html.H5(id='series-time')],width=12)]),
            dbc.Row([

                dbc.Col([                
                    dbc.Row(dbc.Col(dcc.Graph(id='wave-graph'))),
                ]),

                dbc.Col([                
                    dbc.Row(dbc.Col(dcc.Graph(id='wind-graph'))),
                ]),
                
                dbc.Col([
                    dbc.Row(dbc.Col(dcc.Graph(figure={},id='map-graph'))),
                    ]),
            ])
        ])
        )


    @dash.callback(Output('wave-graph', 'figure'),
            Input('map-interval', 'n_intervals'))
    def waveheight_plots(self,_n):
        """_summary_

        Args:
            n: int : interval input that activates callback (unused)

        Returns:
            fig: figure
        """

        greenish = "rgba(0, 128, 0, 0.55)"
        yellowish = "rgba(180, 180, 0, 0.45)"
        orangish = "rgba(255, 119, 0, 0.5)"
        reddish = "rgba(200, 0, 0, 0.5)"

        fig = make_subplots(
            rows=7, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.05,
            horizontal_spacing=0.03)

        for buoy in (BUOY_IDS):
            buoy_dataframe = self.buoys.data[buoy]
            row = BUOY_DICT[buoy]['row']
            buoy_title = BUOY_DICT[buoy]['title']
            #buoy_color = BUOY_DICT[buoy]['color']

            this_line_dict = {}
            this_line_dict['color'] = 'rgba(255, 255, 255, 1)'
            this_line_dict['width'] = 3.5
            this_line_dict['dash'] = 'solid'

            fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_dataframe['WVHT'], name=buoy_title, text=buoy_title, line=this_line_dict, hovertemplate = '%{y:.2f} ft'), row=row, col=1)   
            fig.add_hrect(y0=self.buoys.min_speed, y1=min(self.buoys.max_speed,21.5), fillcolor=greenish, line_width=0, row=r, col=1)
            if self.buoys.max_speed > 21.5:
                fig.add_hrect(y0=21.5, y1=min(self.buoys.max_speed,33.5), fillcolor=yellowish, line_width=0, row=r, col=1)
            if self.buoys.max_speed > 33.5:
                fig.add_hrect(y0=33.5, y1=min(self.buoys.max_speed,47.5), fillcolor=orangish, line_wiseldth=0, row=r, col=1)
            if self.buoys.max_speed > 47.5:
                fig.add_hrect(y0=47.5, y1=min(self.buoys.max_speed,63), fillcolor=reddish, opacity=1, line_width=0, row=r, col=1)
            fig.add_vline(x=self.times.now, line=dict(dash="solid", width=2, color='white'), row=r, col=1)
            fig.add_vline(x=self.times.now, line=dict(dash="solid", width=2, color='white'), row=r, col=1)
            fig.update_xaxes(range=[self.times.start_time, self.times.end_time])
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
        wave_range = dict(range=[self.buoys.min_height, self.buoys.max_height])
        fig.update_layout(yaxis1 = wave_range)
        fig.update_layout(hovermode="x unified")
        fig.update_layout(title_x=0.08)


 


        


        wave_range = dict(range=[self.buoys.min_height, self.buoys.max_height])
        fig.update_layout(yaxis1 = wave_range)
        fig.update_layout(yaxis2 = wave_range)
        fig.update_layout(yaxis3 = wave_range)
        fig.update_layout(yaxis4 = wave_range)
        fig.update_layout(yaxis5 = wave_range)
        fig.update_layout(yaxis6 = wave_range)
        fig.update_layout(yaxis7 = wave_range)
        fig.update_traces(textposition='top right')
        fig.update_shapes(layer="below")
        return fig

    @dash.callback(Output('wind-graph', 'figure'),
            Input('map-interval', 'n_intervals'))
    def wind_plots(self,_n):
        """_summary_
        """

        fig = make_subplots(
            rows=7, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.05,
            horizontal_spacing=0.03)

        elements = ['WSPD','GST']
        for buoy in (BUOY_IDS):
            buoy_dataframe = self.buoys.data[buoy]
            row = BUOY_DICT[buoy]['row']
            buoy_title = BUOY_DICT[buoy]['title']
            #buoy_color = BUOY_DICT[buoy]['color']

            this_line_dict = {}
            this_line_dict['color'] = 'rgba(255, 255, 255, 1)'
            this_line_dict['width'] = 3.5
            this_line_dict['dash'] = 'solid'
            fig.update_xaxes(range=[self.times.start_time, self.times.end_time])
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
        wind_range = dict(range=[self.buoys.min_speed, self.buoys.max_speed])

        fig.update_layout(yaxis2 = wind_range)
        fig.update_layout(hovermode="x unified")
        fig.update_layout(title_x=0.08)

        greenish = "rgba(0, 128, 0, 0.55)"
        yellowish = "rgba(180, 180, 0, 0.45)"
        orangish = "rgba(255, 119, 0, 0.5)"
        reddish = "rgba(200, 0, 0, 0.5)"
        for r in range(1,8):
            for element in elements:
                if element == 'WSPD':
                    this_marker_dict=dict(color=this_line_dict['color'], size=7)
                    #fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, text=buoy_title, line=this_line_dict, hovertemplate = '%{y:.0f} kt'), row=row, col=2)
                    fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, mode="markers", marker=this_marker_dict, hovertemplate = '%{y:.0f} kt'), row=row, col=2)
                if element == 'GST':
                    grayish = "rgba(215, 215, 215, 1)"
                    this_line_dict['color'] = grayish
                    this_marker_dict=dict(color=this_line_dict['color'], size=4)
                    fig.add_trace(go.Scatter(x=buoy_dataframe.index, y=buoy_element, name=buoy_title, mode="markers", marker=this_marker_dict, hovertemplate='G %{y:.0f} kt'), row=row, col=2)
            fig.add_hrect(y0=self.buoys.min_speed, y1=min(self.buoys.max_speed,21.5), fillcolor=greenish, line_width=0, row=r, col=1)
            if self.buoys.max_speed > 21.5:
                fig.add_hrect(y0=21.5, y1=min(self.buoys.max_speed,33.5), fillcolor=yellowish, line_width=0, row=r, col=1)
            if self.buoys.max_speed > 33.5:
                fig.add_hrect(y0=33.5, y1=min(self.buoys.max_speed,47.5), fillcolor=orangish, line_width=0, row=r, col=1)
            if self.buoys.max_speed > 47.5:
                fig.add_hrect(y0=47.5, y1=min(self.buoys.max_speed,63), fillcolor="pink", opacity=1, line_width=0, row=r, col=1)
            fig.add_vline(x=self.times.now, line=dict(dash="solid", width=2, color='white'), row=r, col=1)
            fig.add_vline(x=self.times.now, line=dict(dash="solid", width=2, color='white'), row=r, col=1)

        wind_range = dict(range=[self.buoys.min_speed, self.buoys.max_speed])
        fig.update_layout(yaxis1 = wind_range)
        fig.update_layout(yaxis2 = wind_range)
        fig.update_layout(yaxis3 = wind_range)
        fig.update_layout(yaxis4 = wind_range)
        fig.update_layout(yaxis5 = wind_range)
        fig.update_layout(yaxis6 = wind_range)
        fig.update_layout(yaxis7 = wind_range)

        fig.update_traces(textposition='top right')
        fig.update_shapes(layer="below")
        return fig


def main() -> None:
    plot_times = PlotTimes(3, 10)

if __name__ == "__main__":
    main()
