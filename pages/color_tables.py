# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
    path='/colortables',
    title='Color Tables',
    name='Color Tables',
    order=4)

title = dbc.Container([
        html.Br(),
        dbc.Row([dbc.Col(html.H2("GR2Analyst Color Tables"), width=12)])
    ])
bullet_list = dbc.Container(dbc.Col(
    html.Ul([
        html.Li(html.A("HSLuv website", \
        href="https://www.hsluv.org/")),
    ])
))

# Define the page layout
def layout():
    """
    Color Tables page layout
    """
    return dbc.Container([title, bullet_list])

