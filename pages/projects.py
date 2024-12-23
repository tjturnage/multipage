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
    name='Projects',
    order=6)


def layout():
    """
    Temp layout
    """
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.H1("Open Source Rocks!"),
                        width=12,
                    ),
                ]
            )
        ]
    )

