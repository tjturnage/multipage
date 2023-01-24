# Import necessary libraries 
import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)


top_content = [
            dbc.CardBody([html.H1("T.J. Turnage", className="card-title,text-center",style={'font-weight': 'bold', 'font-style': 'italic'}),
                html.Div([
                dbc.CardLink("GitHub", href="https://github.com/tjturnage")]),
                html.Div([
                dbc.CardLink("@turnageweather", href="https://twitter.com/turnageweather")]),])
]

# Define the page layout


layout = dbc.Container(
    dbc.Container(
        html.Div([
            dbc.Row(dbc.Col(html.Div(html.Hr()))),
            dbc.Row(dbc.Card(top_content, color="secondary", inverse=True))
        ],className="text-center")
))
# layout = html.Div(
#     [
#         dcc.Markdown("# T.J. Turnage", style={"textAlign": "center"}),
#         dcc.Markdown("Grand Rapids, MI USA", style={"textAlign": "center"}),
#         dcc.Markdown("### About", style={"textAlign": "center"}),
#         html.Hr(),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [
#                         dcc.Markdown(
#                             """
#             * Saved by Grace 
#             * Husband
#             * Father
#             """
#                         )
#                     ],
#                     width={"size": 3, "offset": 1},
#                 ),
#                 dbc.Col(
#                     [
#                         dcc.Markdown(
#                             """
#             * Meteorologist 
#             * Bass player
#             * Python dilettante
#             """
#                         )
#                     ],
#                     width=3,
#                 ),
#             ],
#             justify="center",
#         ),
#         html.Hr(),
#         dcc.Markdown("### Professional Summary", style={"textAlign": "center"}),
#         html.Hr(),
#         dcc.Markdown(
#             "Science and Operations Officer \n"
#             "Bringing new science and technology into operational meteorology ...",
#             style={"textAlign": "center", "white-space": "pre"},
#         ),
#         html.Hr(),
#         dcc.Markdown("### Skills", style={"textAlign": "center"}),
#         html.Hr(),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [
#                         dcc.Markdown(
#                             """
#             * Python 
#             * Web development
#             """
#                         )
#                     ],
#                     width={"size": 3, "offset": 1},
#                 ),
#                 dbc.Col(
#                     [
#                         dcc.Markdown(
#                             """
#             * Image processing (GIMP)
#             """
#                         )
#                     ],
#                     width=3,
#                 ),
#             ],
#             justify="center",
#         ),
#         html.Hr(),
#         dcc.Markdown("### Work History", style={"textAlign": "center"}),
#         html.Hr(),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [dcc.Markdown("Jan 2006 - present", style={"textAlign": "center"})],
#                     width=2,
#                 ),
#                 dbc.Col(
#                     [
#                         dcc.Markdown(
#                             "Science and Operations Officer \n"
#                             "NOAA/National Weather Service - Grand Rapids, MI",
#                             style={"white-space": "pre"},
#                             className="ms-3",
#                         ),
#                         html.Ul(
#                             [
#                                 html.Li(
#                                     "Bringing new science into operational meteorology"
#                                 ),
#                             ]
#                         ),
#                     ],
#                     width=5,
#                 ),
#             ],
#             justify="center",
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [dcc.Markdown("Nov 1998 - Jan 2006", style={"textAlign": "center"})],
#                     width=2,
#                 ),
#                 dbc.Col(
#                     [
#                         dcc.Markdown(
#                             "Senior Meteorologist \n"
#                             "NOAA/National Weather Service - Tallahassee, FL",
#                             style={"white-space": "pre"},
#                             className="ms-3",
#                         ),
#                         html.Ul(
#                             [
#                                 html.Li(
#                                     "Team leader for timely and accurate observations, forecasts, and warnings for parts of FL, GA, and AL"
#                                 ),

#                             ]
#                         ),
#                     ],
#                     width=5,
#                 ),
#             ],
#             justify="center",
#         ),
#         html.Hr(),
#         dcc.Markdown("### Education", style={"textAlign": "center"}),
#         html.Hr(),
#         dbc.Row(
#             [
#                 dbc.Col([dcc.Markdown("1991", style={"textAlign": "center"})], width=2),
#                 dbc.Col(
#                     [
#                         dcc.Markdown(
#                             "Bachelor of Science: Meteorology\n"
#                             "Iowa State University - Ames, IA",
#                             style={"white-space": "pre"},
#                             className="ms-3",
#                         ),
#                     ],
#                     width=5,
#                 ),
#             ],
#             justify="center",
#         ),
#                 dbc.Row(
#             [
#                 dbc.Col([dcc.Markdown("2007", style={"textAlign": "center"})], width=2),
#                 dbc.Col(
#                     [
#                         dcc.Markdown(
#                             "Master of Science: Meteorology\n"
#                             "Florida State University - Tallahassee, FL",
#                             style={"white-space": "pre"},
#                             className="ms-3",
#                         ),
#                     ],
#                     width=5,
#                 ),
#             ],
#             justify="center",
#         ),
#     ]
# )

# # ----------------------------------------
# #        Show Text output window
# # ----------------------------------------
# #@app.callback(
# #    Output("display-file-content-response", "children"),
# #    Input("display-file-content-btn","n_clicks"),
# #    prevent_initial_call=True,
# #)
# # The html default for object element width is way too small.
# # Thus, there is a "assets/object.css" file that overrides the defaults

# #def show_file_content(n_clicks):
# #    return [html.ObjectEl(data="https://fsw.nws.noaa.gov/assets/output.txt")]