# Import necessary libraries 
import dash
from dash import html #, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__,
    path='/afds',
    title='Area Forecast Discussions',
    name='AFDs',
    order=1)

# Define the page layout
def layout():
    """Area Forecast Discussions page layout

    Returns:
        None
    """
    return dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div([
                html.Div(children=[html.ObjectEl( \
                data="https://tjturnage.pythonanywhere.com/assets/afds.txt")], \
                id="display-file-content-response",
                style={'height':'800px'})
                ],
                style={'padding':'1em',
                       'height':'900px'})
            )
        ],style={'padding':'0.5em',
                 'height':'900px'}),
        ])
