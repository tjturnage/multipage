# Import necessary libraries 
import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__,
    path='/afds',
    title='Area Forecast Discussions',
    name='Area Forecast Discussions')

# Define the page layout
def layout():
    return dbc.Container([
    dbc.Row([
        html.Center(html.H1("AFDs")),
        html.Br(),
        html.Hr(),
        dbc.Col([
            html.Div("Area Forecast Discussions from NWS GRR"),
            html.Div("<pre><object data='assets/afds.txt'></object></pre>")
        ])
    ])
])

# ----------------------------------------
#        Show Text output window
# ----------------------------------------

# The html default for object element width is way too small.
# Thus, there is a "assets/object.css" file that overrides the defaults

def show_file_content(n_clicks):
    return [html.ObjectEl(data="assets/afds.txt")]