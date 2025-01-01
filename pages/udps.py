# Import necessary libraries 
import sys
import dash
from dash import html
import dash_bootstrap_components as dbc

if sys.platform.startswith('win'):
    url = 'http://localhost:8050/assets/json.txt'
else:
    url = 'https://turnageweather.us/assets/json.txt'

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
        html.Li(html.A("Model Sounding URL Example", \
        href= \
    "https://mesonet.agron.iastate.edu/api/1/nws/bufkit.json?time=2024-05-07T22:02:00&lon=-85.54&lat=42.89&gr=1", \
        target="_blank")),
        html.Li(html.A("Model Sounding Template", \
        href="assets/json.txt", target="_blank")),
    ])
))


paragraph1 = html.P("When you click the Model Sounding URL Example link above, you'll get an \
    example of what GR2A uses for environmental soundings. This file can be downloaded and \
    then edited to change the time attribute. By adding a couple of minutes to the hour \
    it becomes possible to override the automaticallly updating soundings that GR2Analyst \
    leverages.", style={"text-align": "left"})

paragraph2 = html.P("The lat and lon values are not used. Rather, this environmental sounding \
    gets mapped to whichever radar site is currently selected in GR2Analyst. The only fields \
    that GR2Analyst care about are pressure, height, and temperature. This is why the Model \
    Sounding Template linked above still works, in spite of not including dewpoint or wind \
    data. This file can be used to test height/temperature-aware UDPs", \
    style={"text-align": "left"})


# Define the page layout
def layout():
    """
    User Defined Products page layout
    """
    return dbc.Container([title, bullet_list, paragraph1, paragraph2])

