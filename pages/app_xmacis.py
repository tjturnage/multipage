import dash
from dash import html
import dash_bootstrap_components as dbc
from .side_bar import sidebar

dash.register_page(__name__,
    title='Xmacis plot',
    name='Xmacis plot', order=2)
def layout():
    return html.Div([
        dbc.Row(
            [
                dbc.Col(
                    [
                        sidebar()
                    ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

                dbc.Col(
                    [
                        html.H3('Starting an xmacis plot interface', style={'textAlign':'center'}),
                    ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
            ]
        )
    ])
