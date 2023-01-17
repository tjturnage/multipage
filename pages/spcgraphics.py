# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

### Add the page components here 

# Define the final page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("SPC Graphics")),
        html.Br(),
        html.Hr(),
        html.Div([
            html.P("Hi!")
        ])
        #dbc.Col([
        #    html.P("This is column 1."), 
        #    dbc.Button("Test Button", color="secondary")
        #]), 

        ])
    ])
