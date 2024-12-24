# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
    path='/udps',
    title='User Defined Products',
    name='User Defined Products',
    order=3)

title = dbc.Container([
        html.Br(),
        dbc.Row([dbc.Col(html.H2("GR2Analyst User Defined Products"), width=12)])
    ])
bullet_list = dbc.Container(dbc.Col(
    html.Ul([
        html.Li(html.A("UDP User Guide", \
        href="https://www.grlevelx.com/downloads/UserDefinedProducts_3.pdf")),
    ])
))

# Define the page layout
def layout():
    """
    User Defined Products page layout
    """
    return dbc.Container([title, bullet_list])

