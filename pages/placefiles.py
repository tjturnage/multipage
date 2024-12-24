# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
    path='/placefiles',
    title='Placefiles',
    name='Placefiles',
    order=2)

title = dbc.Container([
        html.Br(),
        dbc.Row([dbc.Col(html.H2("GR2Analyst Placefiles"), width=12)])
    ])
bullet_list = dbc.Container(dbc.Col(
    html.Ul([
        html.Li(html.A("Surface Obs", \
        href="assets/latest_surface_observations.txt")),
        html.Li(html.A("Surface Obs - large font", \
        href="assets/latest_surface_observations_lg.txt")),
        html.Li(html.A("Surface Obs - extra large font", \
        href="assets/latest_surface_observations_xlg.txt")),
        html.Li(html.A("Air Temperature", \
        href="assets/temp.txt")),
        html.Li(html.A("Dewpoint Temperature", \
        href="assets/dwpt.txt")),
        html.Li(html.A("MI Road Temperature", \
        href="assets/road.txt")),
        html.Li(html.A("Wind and Gust", \
        href="assets/wind.txt")),
    ])
))

# Define the page layout
def layout():
    """mesoanalysis page layout

    Returns:
        None
    """
    return dbc.Container([title, bullet_list])

