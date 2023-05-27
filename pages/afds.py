# Import necessary libraries 
import dash
from dash import html #, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__,
    path='/afds',
    title='Area Forecast Discussions',
    name='Area Forecast Discussions')

# Define the page layout
def layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div([
                    #dbc.Button("Show File Content", id="display-file-content-btn", color="success", style={'padding':'1em','width':'100%'}),
                    html.Div(children=[html.ObjectEl(data="https://tjturnage.pythonanywhere.com/multipage/assets/afds.txt")],id="display-file-content-response")
                ],
                style={'padding':'1em'})
            )
        ],style={'padding':'0.5em'}),
        ])

# ----------------------------------------
#        Show Text output window
# ----------------------------------------

# The html default for object element width is way too small.
# Thus, there is a "assets/object.css" file that overrides the defaults

#@callback(
#    Output("display-file-content-response", "children"),
#    Input("display-file-content-btn","n_clicks"),
#    prevent_initial_call=True,
#)
# The html default for object element width is way too small.
# Thus, there is a "assets/object.css" file that overrides the defaults

#def show_file_content(n_clicks):
#    return [html.ObjectEl(data="https://tjturnage.pythonanywhere.com/assets/afds.txt")]