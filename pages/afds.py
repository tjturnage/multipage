# Import necessary libraries 
import dash
from dash import html #, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__,
    path='/afds',
    title='Area Forecast Discussions',
    name='GRR AFDs',
    order=1)

# Define the page layout
def layout():
    """Area Forecast Discussions page layout

    Note: the dimensions of the html.ObjectEl are defined by object.css in the assets folder
    """
    return dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div([
                html.Div(children=[html.ObjectEl( \
                data="https://www.turnageweather.us/assets/afds.txt")], \
                id="display-file-content-response",
                style={'padding':'1em',
                       'height':'1200px'})
                ],
                style={'padding':'1em',
                       'height':'1200px'})
            )
        ])
        ])
