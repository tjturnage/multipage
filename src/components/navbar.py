"""
This defines the navbar at the top
"""
# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def navbar():
    """
    Top navbar components are listed here
    """

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("AFDs", href="/afds")),
            ] ,
            brand="turnageweather",
            brand_href="/home",
            color="dark",
            dark=True,
        ),
    ])

    return layout
