"""
Main projects page is the graffitti page
"""
import sys
from pathlib import Path
import dash
import dash_bootstrap_components as dbc
from dash import html

if sys.platform.startswith('win'):
    p = Path('C:/data/scripts')
else:
    p = Path('/home/tjturnage')


dash.register_page(__name__,
                   path='/projects',
    title='Open Source',
    name='Open Source')

title = dbc.Container([
        html.Br(),
        dbc.Row([dbc.Col(html.H2("(Mostly) Open Source Projects"), width=12)])
    ])

content = dbc.Container(
    dbc.Row(
        dbc.Col(
            [
                html.H1("Software I'm currently messing with"),
                html.Ul(
                    [
                        html.Li("Inkscape"),
                        html.Li("GIMP"),
                        html.Li("Blender"),
                        html.Li("Audacity"),
                        html.Li("Obs Studio"),
                    ]
                )
            ],
            width=12,
        )
    )
)


def layout():
    """
    Layout of projects page
    """
    return dbc.Container([title, content])
